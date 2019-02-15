#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import datetime
import scrapy
from scrapy_redis.spiders import RedisSpider,RedisCrawlSpider
from scrapy_splash import SplashRequest
from myspider.downloaders import selenium,requests,splash
from myspider.pipelines.FangchanItem import *

'''
继承自RedisSpider，则start_urls可以从redis读取，爬虫初次运行是空队列等待，给redis添加数据后开始爬取
抛出SplashRequest请求，则不采用scrapy自身的downloader（很容易被反爬），而是访问splash服务的httpAPI，返回对应的网页
'''


class fangchan_anjuke_zufang_spider(RedisSpider):
    name = 'fangchan_anjuke_zufang'
    custom_settings = {
        'PROXY_ENABLE': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC':True,
    }
    browser = None

    def make_requests_from_url(self, url):
        # 此方法重写RedisSpider的默认方法
        # 功能：从redis中取出url后，如何把url转换为Request请求（默认为scrapy原生请求，这里要改为splash的请求）
        return SplashRequest(url, endpoint='render.html', callback=self.parse, args={'wait': 3, 'html': 1})

    def parse(self, response):
        # 安居客有反爬措施，用scrapy原生下载器几乎全是302重定向，这里使用splash
        # if not self.browser:
        #     self.browser = selenium.Chrome().load()
        # self.browser.get(response.request.url)
        # time.sleep(3)
        # response = scrapy.Selector(text=self.browser.page_source)
        # self.browser.close()
        list_content = response.css('.list-content .zu-itemmod')
        for iter in list_content:
            item = fangchan_anjuke_zufang_item()
            item.parse_listpage(response, iter)
            url_detailpage=response.css('.zu-itemmod div::attr(link)').extract_first()
            # 发出爬取项目详情页请求
            yield SplashRequest(url=url_detailpage, endpoint='render.html', callback=self.parsedetail, meta={'data': item})
        url_nextpage=response.css('.aNxt::attr(href)').extract_first()
        # 发出爬取下一页列表请求
        yield SplashRequest(url=url_nextpage, endpoint='render.html', callback=self.parse)

    # callback回调链可在一个爬虫里递进深入爬取
    def parsedetail(self, response):
        item = response.meta['data']  #把之前的未完成爬取结果传递过来继续补充完整
        item.parse_detailpage(response)
        item.crawl_time = datetime.datetime.today()
        print('spider----------------------'+str(item))
        yield item


class fangchan_fangtianxia_zufang_spider(RedisSpider):
    name = 'fangchan_fangtianxia_zufang'
    custom_settings = {
        'PROXY_ENABLE': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC':True,
    }
    browser = None

    def parse(self, response):
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
    name = 'fangchan_58_zufang'
    custom_settings = {
        'PROXY_ENABLE':True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATIC': True,
    }
    browser = None

    def parse(self, response):
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
