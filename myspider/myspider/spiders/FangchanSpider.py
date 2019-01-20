#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy_splash import SplashRequest
from myspider.downloaders import selenium,requests
from myspider.pipelines.FangchanItem import *

'''
继承自RedisSpider，则start_urls可以从redis读取
抛出SplashRequest请求，则不采用scrapy自身的downloader（很容易被反爬），而是访问splash服务的httpAPI，返回对应的网页
'''


class fangchan_anjuke_zufang_spider(RedisSpider):
    count = {'all':0, 'success':0, 'failed':0}
    name = 'fangchan_anjuke_zufang'
    allowed_domains = ['anjuke.ccom']
    custom_settings = {
        'PROXY_ENABLE': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC':True,
    }
    browser = None

    def parse(self, response):
        if response.status == 200:  # 如果是200成功说明scrapy可以得到正确网页，否则需要使用requests或selenium避免反爬
            pass
        elif response.status == 302:  # 安居客有反爬措施，几乎全是302重定向
            if not self.browser:
                self.browser = selenium.Chrome().load()
            self.browser.get(response.request.url)
            time.sleep(3)
            response = scrapy.Selector(text=self.browser.page_source)
            self.browser.close()
        list_content = response.css('.list-content .zu-itemmod')
        for iter in list_content:
            item = fangchan_anjuke_zufang_item()
            item.parse_listpage(response, iter)
            url_detailpage=response.css('.zu-itemmod div::attr(link)').extract_first()
            print('----------------------'+str(item))
            yield scrapy.Request(url=url_detailpage,callback=self.parsedetail)
            yield item
        url_nextpage=response.css('.aNxt::attr(href)').extract_first()
        yield scrapy.Request(url=url_nextpage)

    # callback回调链可在一个爬虫里递进深入爬取
    def parsedetail(self, response):
        if response.status == 200:
            item = fangchan_anjuke_zufang_item()
            item.parse_detailpage(response)
            print('----------------------'+str(item))
            yield item
        elif response.status == 302:
            pass


class fangchan_fangtianxia_zufang_spider(RedisSpider):
    count = {'all': 0, 'success': 0, 'failed': 0}
    name = 'fangchan_fangtianxia_zufang'
    allowed_domains = ['fang.com']
    custom_settings = {
        'PROXY_ENABLE': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC':True,
    }

    def parse(self, response):
        if response.status==200:
            self.count['success']+=1
            print("success num:"+str(self.count['success']))
        list_content = response.css('.list-content .zu-itemmod')
        for i in list_content:
            item = fangchan_fangtianxia_zufang_item()
            item.parse_listpage(response, i)
            url_detailpage = response.css('.zu-itemmod div::attr(link)').extract_first()
            print('----------------------' + str(item))
            yield scrapy.Request(url=url_detailpage, callback=self.parsedetail)
            yield item
        url_nextpage = response.css('.aNxt::attr(href)').extract_first()
        yield scrapy.Request(url=url_nextpage)

    def parsedetail(self, response):
        item = fangchan_fangtianxia_zufang_item()
        item.parse_detailpage(response)
        print('----------------------'+str(item))
        yield item


class fangchan_58_zufang_spider(RedisSpider):
    count = {'all': 0, 'success': 0, 'failed': 0}
    name = 'fangchan_58_zufang'
    allowed_domains = ['58.com']
    custom_settings = {
        'PROXY_ENABLE':True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC': True,
    }

    def parse(self, response):
        if response.status == 200:
            self.count['success'] += 1
            print("success num:" + str(self.count['success']))
        list_content = response.css('.list-content .zu-itemmod')
        for i in list_content:
            item = fangchan_wubatongcheng_zufang_item()
            item.parse_listpage(response, i)
            url_detailpage = response.css('.zu-itemmod div::attr(link)').extract_first()
            print('----------------------' + str(item))
            yield scrapy.Request(url=url_detailpage, callback=self.parsedetail)
            yield item
        url_nextpage = response.css('.aNxt::attr(href)').extract_first()
        yield scrapy.Request(url=url_nextpage)

    def parsedetail(self, response):
        item = fangchan_wubatongcheng_zufang_item()
        item.parse_detailpage(response)
        print('----------------------' + str(item))
        yield item
