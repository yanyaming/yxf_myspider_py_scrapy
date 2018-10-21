# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
import scrapy


class AnjukeSpider(scrapy.Spider):
    name = 'fangchan-anjuke'
    allowed_domains = ['anjuke.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'myspider.pipelines.UrlQueuePipeline': 300
        }
    }
    start_urls = ['https://wx.fang.anjuke.com/loupan/all/']

    def parse(self, response):
        pass

class FangtianxiaSpider(scrapy.Spider):
    name = 'fangchan-fangtianxia'
    allowed_domains = ['fang.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'myspider.pipelines.UrlQueuePipeline': 300
        }
    }
    start_urls = ['http://wuxi.newhouse.fang.com/house/s/']

    def parse(self, response):
        pass
