#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
import traceback
import time
from scrapy import Selector
from scrapy.http import HtmlResponse,TextResponse
from scrapy.exceptions import IgnoreRequest
from myspider.downloaders import myselenium

'''
每次请求的异常处理，放行正确的请求与响应，对出错的请求选择重新加入队列或者丢弃
'''


class MyHandlerMiddleware(object):
    browser = None

    # 截获下载中间件抛出的所有异常（请求阶段）。twisted的异常类型：多为传输层TCP的timeout或者refused
    def process_exception(self, request, exception, spider):
        PROXY_ENABLE = spider.settings.get('PROXY_ENABLE', False)

        if PROXY_ENABLE:
            if 'proxy_failed_times' in request.meta:
                request.meta['proxy_failed_times'] += 1
        spider.logger.info('MyHandlerMiddleware----------downloader GET failed')
        return request.replace(dont_filter=True)  # 重新把请求加入队列并设置不被筛选掉
        # raise exception

    # 截获爬虫中间件抛出的所有异常（响应阶段）
    def process_spider_exception(self, response, exception, spider):
        PROXY_ENABLE = spider.settings.get('PROXY_ENABLE',False)

        if PROXY_ENABLE:
            response.request.meta['proxy_failed_times'] += 1
        spider.logger.info('MyHandlerMiddleware----------spider GET failed')
        # return response.request.replace(dont_filter=True)
        raise exception

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
            if not self.browser:
                if PROXY_ENABLE:
                    self.browser = myselenium.load_firefox(load_images=False, display=True, proxy=request.meta['proxy'].decode('utf-8'))
                else:
                    self.browser = myselenium.load_firefox(load_images=False,display=True)
            self.browser.get(request.url)
            res = TextResponse(url=self.browser.current_url,body=bytes(self.browser.page_source,encoding='utf-8'))
            # self.browser.close()
            return TextResponse(url=request.url, status=200, headers=response.headers,
                                body=res.body, request=request)
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