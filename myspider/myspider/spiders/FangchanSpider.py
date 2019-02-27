#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
from scrapy import Request
from scrapy.http.headers import Headers
import json
from scrapy.spiders import Spider
from scrapy_redis.spiders import RedisSpider
from scrapy_splash import SplashRequest
from myspider.items.FangchanItem import *

'''
继承自RedisSpider，则start_urls可以从redis读取，爬虫初次运行是空队列等待，给redis添加数据后开始爬取
'''


#1
class fangchan_anjuke_zufang_spider(RedisSpider):
    name = 'fangchan_anjuke_zufang'
    custom_settings = {
        'PROXY_ENABLE': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC':True,
        'CUSTOM_DOWNLOADER':'requests',
    }

    def parse(self, response):
        list_content = response.css('.list-content .zu-itemmod')
        for ite in list_content:
            item = fangchan_anjuke_zufang_item()
            item.parse_listpage(response, ite)
            url_detailpage=response.css('.zu-itemmod::attr(link)').extract_first()
            # 发出爬取项目详情页请求
            yield Request(url=url_detailpage, callback=self.parsedetail, meta={'data': item})
        url_nextpage=response.css('.aNxt::attr(href)').extract_first()
        # 发出爬取下一页列表请求
        yield Request(url=url_nextpage, callback=self.parse)

    # callback回调链可在一个爬虫里递进深入爬取
    def parsedetail(self, response):
        item = response.meta['data']  #把之前的未完成爬取结果传递过来继续补充完整
        item.parse_detailpage(response)
        item['crawl_time'] = datetime.datetime.today()
        yield item


#4
class fangchan_fangtianxia_zufang_spider(RedisSpider):
    name = 'fangchan_fangtianxia_zufang'
    custom_settings = {
        'PROXY_ENABLE': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC':True,
        'CUSTOM_DOWNLOADER':'requests',
    }

    def parse(self, response):
        list_content = response.css('.list-content .zu-itemmod')
        for ite in list_content:
            item = fangchan_fangtianxia_zufang_item()
            item.parse_listpage(response, ite)
            url_detailpage = response.css('.zu-itemmod::attr(link)').extract_first()
            yield Request(url=url_detailpage, callback=self.parsedetail, meta={'data': item})
        url_nextpage = response.css('.aNxt::attr(href)').extract_first()
        yield Request(url=url_nextpage, callback=self.parse)

    def parsedetail(self, response):
        item = fangchan_fangtianxia_zufang_item()
        item.parse_detailpage(response)
        item['crawl_time'] = datetime.datetime.today()
        yield item


#7
class fangchan_wubatongcheng_zufang_spider(RedisSpider):
    name = 'fangchan_wubatongcheng_zufang'
    custom_settings = {
        'PROXY_ENABLE': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC':True,
        'CUSTOM_DOWNLOADER':'requests',
    }

    def parse(self, response):
        list_content = response.css('.list-content .zu-itemmod')
        for ite in list_content:
            item = fangchan_wubatongcheng_zufang_item()
            item.parse_listpage(response, ite)
            url_detailpage = response.css('.zu-itemmod::attr(link)').extract_first()
            yield Request(url=url_detailpage, callback=self.parsedetail, meta={'data': item})
        url_nextpage = response.css('.aNxt::attr(href)').extract_first()
        yield Request(url=url_nextpage)

    def parsedetail(self, response):
        item = fangchan_wubatongcheng_zufang_item()
        item.parse_detailpage(response)
        item['crawl_time'] = datetime.datetime.today()
        yield item
