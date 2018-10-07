# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class UrlQueueItem(scrapy.Item):
    url = scrapy.Field()

class data_redis_mongodb(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    place = scrapy.Field()
    types = scrapy.Field()
    num = scrapy.Field()

