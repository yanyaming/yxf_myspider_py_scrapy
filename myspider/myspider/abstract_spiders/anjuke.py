# -*- coding: utf-8 -*-
import scrapy


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'myspider.pipelines.UrlQueuePipeline': 300
        }
    }
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        pass
