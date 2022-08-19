# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_jsonschema.item import JsonSchemaItem

class CrawlerItem(JsonSchemaItem):
	jsonschema =     {
		"$schema": "http://json-schema.org/draft-04/schema#",
		"title": "Article",
		"description": "A article",
		"type": "object",
		"properties": {
			"date": {
				"type": "string"
			},
			"name": {
				"type": "string"
			},
			"link": {
				"type": "string",
			},
			"labels": {
				"type": "array",
			},
			"content": {
				"type": "string",
			},
		},
		"required": ["date", "name", "link", "labels", "content",]
	}
