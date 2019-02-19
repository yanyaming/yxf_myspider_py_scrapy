#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from myspider.downloaders import selenium
from scrapy.http import HtmlResponse,Response,Request
from scrapy.exceptions import IgnoreRequest


class MyDownloaderMiddleware(object):
    browser = None

    def process_request(self, request, spider):
        DOWNLOADER = spider.settings.get('DOWNLOADER', 'default')
        response = None

        if DOWNLOADER == 'default':
            pass
        elif DOWNLOADER == 'requests':
            response = requests.get(url=request.url,headers=request.headers)
        elif DOWNLOADER == 'phantomjs':
            pass
        elif DOWNLOADER == 'chorme':
            pass

        return Response(url=request.url,status=response.status,headers=response.headers,body=response.body)
