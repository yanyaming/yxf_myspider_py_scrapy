# -*- coding: utf-8 -*-
from scrapy import signals


class MyspiderSpiderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # scrapy风格的实例化入口，功能类似__init__，在__init__之前执行，会自动生成crowler和settings属性
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):
        # 爬虫实例开始运行的初始动作
        spider.logger.info('Spider opened: %s' % spider.name)

    def process_start_requests(self, start_requests, spider):
        # 爬虫发出请求，递交给下载中间件之前的处理
        #
        # 返回值:
        # Requests
        for r in start_requests:
            yield r

    def process_spider_input(self, response, spider):
        # 处理下载器返回的响应，获取经过下载中间件以后的响应内容，最终移交给爬虫
        #
        # 返回值可选:
        # None:继续传递
        # exception:发出异常，调用各爬虫中间件的process_spider_exception()
        return None

    def process_spider_output(self, response, result, spider):
        # 爬虫处理响应完成之后，接收响应和处理结果，选择返回新的请求或者数据项目
        #
        # 返回值:
        # result:Requests/dicts/Items
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # 处理爬虫以及爬虫中间件读取响应的异常
        #
        # 返回值可选:
        # None:继续传递
        # result:Requests/dicts/Items
        pass


class MyspiderDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # scrapy风格的实例化入口，功能类似__init__，在__init__之后执行，会自动生成crowler和settings属性
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def spider_opened(self, spider):
        # 爬虫实例开始运行的初始动作
        spider.logger.info('Spider opened: %s' % spider.name)

    def process_request(self, request, spider):
        # 爬虫发出请求后接收请求内容，处理请求，最终递交给下载器访问网站
        #
        # 返回值可选：
        # None:继续传递
        # Response:请求在此方法中到达目标网站并获得返回数据或者中止请求，将开始调用中间件的响应处理方法
        # Request:发出新的请求
        # IgnoreRequest:发出异常，调用各下载中间件的process_exception()
        return None

    def process_response(self, request, response, spider):
        # 处理响应，接收下载器访问网站得到的响应，最终传递给爬虫解析
        #
        # 返回值可选：
        # Response:继续传递
        # Request:发出新的请求
        # IgnoreRequest:发出异常，调用各下载中间件的process_exception()
        return response

    def process_exception(self, request, exception, spider):
        # 处理下载器以及下载中间件访问网站和读取响应的异常
        #
        # 返回值可选：
        # None:继续传递
        # Response:返回修正后的响应，继续传递
        # Request:发出新的请求
        pass
