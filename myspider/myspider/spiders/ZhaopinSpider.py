#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from myspider.items.ZhaopinItem import *


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
        self.parselist(response)
        try:
            url_nextpage = response.css('#resultList .dw_page ul').xpath('./li[last()]').extract_first()
            # 发出爬取下一页列表请求
            yield Request(url=url_nextpage, callback=self.parse)
        except:
            return None

    def parselist(self, response):
        list_content = response.css('#resultList .el')
        for ite in list_content:
            item = zhaopin_item()
            item.parse_listpage(response, ite)
            url_detailpage=ite.css('p span a::attr(href)').extract_first()
            # 发出爬取项目详情页请求
            yield Request(url=url_detailpage, callback=self.parsedetail, meta={'data': item})

    def parsedetail(self, response):
        item = response.meta['data']  #把之前的未完成爬取结果传递过来继续补充完整
        item.parse_detailpage_qianchengwuyou(response)
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
