import scrapy
import json
import datetime
from scrapy.selector import Selector
from crawler.items import CrawlerItem

class MainSpider(scrapy.Spider):
    name = 'main'

    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }

    headers = {
        'Accept':' application/json, */*;q=0.1',
        'Accept-Encoding':' gzip, deflate, br',
        'Accept-Language':' en-US,en;q=0.9',
        'Connection':' keep-alive',
        'Content-Type':' application/json',
        'Cookie':' pll_language=en',
        'Referer':' https://nbs.sk/en/press/news-overview/',
        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://nbs.sk/wp-json/nbs/v1/post/list?_locale=user'
        payload = {"lang":"en","limit":30,"offset":0,"filter":{"lang":"en"},"onlyData":False}
        yield scrapy.Request(url, method='POST', headers=self.headers, body=json.dumps(payload))

    def parse(self, response):
        jsonresponse = response.json()
        articles = Selector(text=jsonresponse['html']).xpath('//a[@class="archive-results__item"]').getall()
        for article in articles:
            item = CrawlerItem()
            item['date'] = Selector(text=article).xpath('//div[@class="date"]/text()').get()
            item['link'] = Selector(text=article).xpath('//a/@href').get()
            item['labels'] = Selector(text=article).xpath('//a/*[self::h2 or self::div[contains(@class, "label")]]/text()').getall()
            item['name'] = ' '.join(item['labels'])
            if '//nbs.sk/en/' in item['link'] or 'ecb.europa.eu' in item['link']:
                yield response.follow(item['link'], callback=self.parse_content, meta={'item':item})
            else:
                yield item
                
    def parse_content(self, response):
        item = response.meta['item']
        item['content'] = response.xpath('normalize-space(//div[contains(@class,"nbs-post__content") or contains(@class, "nbs-content") or @class="section" and .//p[@class="ecb-publicationDate"]])').get()
        yield item
