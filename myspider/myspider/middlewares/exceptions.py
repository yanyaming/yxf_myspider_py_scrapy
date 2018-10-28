#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy


class RequestFailMiddleware(object):

    def process_spider_exception(self, response, exception, spider):
        return scrapy.Request(url=response.request.url).replace(dont_filter=True)

    def process_exception(self, request, exception, spider):
        return scrapy.Request(url=request.url).replace(dont_filter=True)

    def process_response(self, request, response, spider):
        http_code = response.status
        #1xx
        if http_code // 100 == 2:
            return response
        #3xx
        if http_code // 100 == 3 and http_code != 304:
            return request.replace(dont_filter=True)
        #4xx
        if http_code // 100 == 4:
            raise scrapy.IgnoreRequest('404')
        #5xx
        if http_code // 100 == 5:
            return request.replace(dont_filter=True)
