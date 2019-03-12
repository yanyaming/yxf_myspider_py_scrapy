#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from myspider.items.FangchanItem import *


#1
class zhaopin_qianchengwuyou(scrapy.Spider):
    name = 'zhaopin_qianchengwuyou'
    custom_settings = {
        'PROXY_ENABLE': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC': True,
        'CUSTOM_DOWNLOADER': 'requests',
    }

    def parse(self, response):
        list_content = response.css('.list-content .zu-itemmod')
        url_nextpage = response.css('.aNxt::attr(href)').extract_first()
        # 发出爬取下一页列表请求
        yield Request(url=url_nextpage, callback=self.parse)
        for ite in list_content:
            item = fangchan_anjuke_zufang_item()
            item.parse_listpage(response, ite)
            url_detailpage=response.css('.zu-itemmod::attr(link)').extract_first()
            # 发出爬取项目详情页请求
            yield Request(url=url_detailpage, callback=self.parsedetail, meta={'data': item})

    def parsedetail(self, response):
        item = response.meta['data']  #把之前的未完成爬取结果传递过来继续补充完整
        item.parse_detailpage(response)
        item['crawl_time'] = datetime.datetime.today().strftime('%Y-%m-%d')
        yield item


#2
class zhaopin_zhilianzhaopin(scrapy.Spider):
    name = 'zhaopin_zhilianzhaopin'

    def parse(self, response):
        pass


#3
class zhaopin_lagouwang(scrapy.Spider):
    name = 'zhaopin_lagouwang'

    def parse(self, response):
        pass


#4
class zhaopin_bosszhipin(scrapy.Spider):
    name = 'zhaopin_bosszhipin'

    def parse(self, response):
        pass
