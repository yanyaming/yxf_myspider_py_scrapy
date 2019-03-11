#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
import traceback
import time
import redis
from scrapy import signals
from scrapy import Selector
from scrapy.exceptions import DontCloseSpider
from scrapy.http import HtmlResponse,TextResponse
from scrapy.exceptions import IgnoreRequest
from myspider.downloaders import myselenium
from myspider.settings import REDIS_URL,REDIS,PROXY_API,PROXY_SERVER

'''
每次请求的异常处理，放行正确的请求与响应，对出错的请求选择重新加入队列或者丢弃
'''

redis_pool = redis.ConnectionPool(host=REDIS['host'], port=int(REDIS['port']), db=int(REDIS['db']),password=REDIS['password'])


class MyHandlerMiddleware(object):
    browser = None

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    # 爬虫启动操作
    def spider_opened(self, spider):
        # 注册到redis，让远程可以查看正在运行的爬虫有哪些
        r = redis.StrictRedis(connection_pool=redis_pool)
        if r.hexists(b'crawler',bytes(spider.name,encoding='utf-8')):
            count = int(str(r.hget(b'crawler',bytes(spider.name,encoding='utf-8')),encoding='utf-8'))
            r.hset(b'crawler',bytes(spider.name,encoding='utf-8'),count+1)
        else:
            r.hset(b'crawler',bytes(spider.name,encoding='utf-8'),1)
        spider.logger.info('MyPrestartMiddleware----------crawler:' + str(r.hget(b'crawler',bytes(spider.name,encoding='utf-8')),encoding='utf-8'))

    # 爬虫关闭操作
    def spider_closed(self,spider):
        # 取消注册
        r = redis.StrictRedis(connection_pool=redis_pool)
        count = int(str(r.hget(b'crawler',bytes(spider.name,encoding='utf-8')),encoding='utf-8'))
        if count <= 1:
            r.hdel(b'crawler',bytes(spider.name,encoding='utf-8'))
        else:
            r.hset(b'crawler',bytes(spider.name,encoding='utf-8'),count-1)
        if self.browser:
            self.browser.close()

    # 截获下载中间件抛出的所有异常（请求阶段）。twisted的异常类型：多为传输层TCP的timeout或者refused
    def process_exception(self, request, exception, spider):
        PROXY_ENABLE = spider.settings.get('PROXY_ENABLE', False)

        if PROXY_ENABLE:
            if 'proxy_failed_times' in request.meta:
                request.meta['proxy_failed_times'] += 1
        spider.logger.info('MyHandlerMiddleware----------downloader GET failed')
        return request.replace(dont_filter=True)  # 重新把请求加入队列并设置不被筛选掉。停止爬虫时防止丢失请求队列
        # raise exception

    # 截获爬虫中间件抛出的所有异常（响应阶段）
    def process_spider_exception(self, response, exception, spider):
        PROXY_ENABLE = spider.settings.get('PROXY_ENABLE',False)

        if PROXY_ENABLE:
            response.request.meta['proxy_failed_times'] += 1
        spider.logger.info('MyHandlerMiddleware----------spider GET failed')
        return response.request.replace(dont_filter=True)  # 重新把请求加入队列并设置不被筛选掉。停止爬虫时防止丢失请求队列
        # raise exception

    # 得到了响应，框架没有抛出异常，但仍然需要根据响应码删选正确结果，必要时需要手动抛出异常
    def process_response(self, request, response, spider):
        PROXY_ENABLE = spider.settings.get('PROXY_ENABLE', False)
        http_code = response.status

        #1xx请求未完成，需要放行
        if http_code // 100 == 1:
            return response
        #2xx成功响应，需要放行
        if http_code // 100 == 2:
            return response
        #3xx重定向，爬虫正常不会出现304未改动重定向，会可能有302暂时重定向（反爬：验证码，空页面）；其他是失败请求，需要重新加入队列
        if http_code // 100 == 3 and http_code != 302:
            spider.logger.info('MyHandlerMiddleware----------status code:'+str(http_code))
            if PROXY_ENABLE:
                request.meta['proxy_failed_times'] += 1
            return request.replace(dont_filter=True)
        if http_code == 302:#无论是验证码页面还是空页面都是反爬措施，都需要使用非原生下载器
            if PROXY_ENABLE:
                request.meta['proxy_failed_times'] += 1
            spider.logger.info('MyHandlerMiddleware----------status code:302')
            try:
                if not self.browser:
                    if PROXY_ENABLE:
                        if not self.browser:
                            self.browser = myselenium.load_firefox(load_images=False, display=False, proxy=request.meta['proxy'].decode('utf-8'))
                    else:
                        if not self.browser:
                            self.browser = myselenium.load_firefox(load_images=False,display=False)
                self.browser.get(request.url)
                res = TextResponse(url=self.browser.current_url,body=bytes(self.browser.page_source,encoding='utf-8'))
                return TextResponse(url=request.url, status=200, headers=response.headers,
                                    body=res.body, request=request)
            except:
                raise DontCloseSpider
        #4xx找不到，可能有部分是反爬虫的误导，404是无效链接所以直接丢掉；其他需要重新加入队列
        if http_code // 100 == 4 and http_code != 404:
            spider.logger.info('MyHandlerMiddleware----------status code:'+str(http_code))
            if PROXY_ENABLE:
                request.meta['proxy_failed_times'] += 1
            return request.replace(dont_filter=True)
        if http_code == 404:#404无效链接
            raise IgnoreRequest(str(http_code))
        #5xx服务器错误，大型网站一般很少出现服务器错误，所以可认为是反爬虫措施，需要重新加入队列
        if http_code // 100 == 5:
            if PROXY_ENABLE:
                request.meta['proxy_failed_times'] += 1
            spider.logger.info('MyHandlerMiddleware----------status code:'+str(http_code))
            return request.replace(dont_filter=True)
