# -*- coding: utf-8 -*-
import scrapy


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        pass
