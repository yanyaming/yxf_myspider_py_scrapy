#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy import Request
from redis import Redis
from scrapy_redis.spiders import RedisSpider
from myspider.items.ZhaopinItem import *


#1
class zhaopin_qianchengwuyou(RedisSpider):
    name = 'zhaopin_qianchengwuyou'
    custom_settings = {
        'PROXY_ENABLE': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC': True,
        'CUSTOM_DOWNLOADER': 'requests',
    }

    def parse(self, response):
        list_content = response.css('#resultList .el')
        for i, ite in enumerate(list_content):
            if i == 0:
                continue
            else:
                url_detailpage = ite.css('p span a::attr(href)').extract_first()
                # 发出爬取项目详情页请求
                yield Request(url=url_detailpage, callback=self.parsedetail)
        try:
            url_nextpage = response.css('#resultList .dw_page ul').xpath('./li[last()]/a/@href').extract_first()
            # 发出爬取下一页列表请求
            yield Request(url=url_nextpage, callback=self.parse)
        except:
            return None

    def parsedetail(self, response):
        item = zhaopin_item()
        item.parse_detailpage_qianchengwuyou(response)
        item['crawl_time'] = datetime.datetime.today().strftime('%Y-%m-%d')
        yield item


#2
class zhaopin_zhilianzhaopin(RedisSpider):
    name = 'zhaopin_zhilianzhaopin'

    def parse(self, response):
        pass


#3
class zhaopin_lagouwang(RedisSpider):
    name = 'zhaopin_lagouwang'

    def parse(self, response):
        pass


#4
class zhaopin_bosszhipin(RedisSpider):
    name = 'zhaopin_bosszhipin'

    def parse(self, response):
        pass
