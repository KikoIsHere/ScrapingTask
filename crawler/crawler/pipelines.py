# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class CrawlerPipeline:
    def __init__(self):
        self.con = sqlite3.connect('task.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS articles(
        id INTEGER PRIMARY KEY,
        date DATE,
        name VARCHAR(255),
        link VARCHAR(255),
        label1 VARCHAR(255),
        label2 VARCHAR(255),
        content TEXT,
        UNIQUE(date, name)
        )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO articles (date, name, link, label1, label2, content) VALUES (?, ?, ?, ?, ?, ?)""",
                        (item['date'], item['name'], item['link'], item['labels'][0], item['labels'][1], item['content'] if item.get('content') else ''))
        self.con.commit()
        return item
