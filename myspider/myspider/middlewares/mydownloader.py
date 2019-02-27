#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from scrapy.http import HtmlResponse,Response,Request,TextResponse
from scrapy.exceptions import IgnoreRequest
from myspider.downloaders import myselenium,myrequests


class MyDownloaderMiddleware(object):
    browser = None
    session = None

    def process_request(self, request, spider):
        CUSTOM_DOWNLOADER = spider.settings.get('CUSTOM_DOWNLOADER', 'default')

        #1.使用scrapy默认下载器（容易被反爬）
        if CUSTOM_DOWNLOADER == 'default':
            return None
        #2.使用requests（不执行js时的最佳下载器）
        elif CUSTOM_DOWNLOADER == 'requests':
            headers = {}#headers格式不兼容，需要转换
            proxies = {}#若有代理则使用
            for key,value in request.headers.items():
                headers[key] = value[0]
            if 'proxy' in request.meta:
                proxy_url = request.meta['proxy'].decode('utf-8')
                if proxy_url.split('://')[0] == 'http':
                    proxies['http'] = proxy_url.split('://')[1]
                elif proxy_url.split('://')[0] == 'https':
                    proxies['https'] = proxy_url.split('://')[1]
            response = myrequests.my_requests_request(method='get',url=request.url,headers=headers,
                                                      proxies=proxies,allow_redirects=False)
            return TextResponse(url=request.url, status=response.status_code, headers=response.headers,
                                body=response.content,request=request)  # content是utf-8编码形式
        #3.使用selenium（模拟浏览器）
        elif CUSTOM_DOWNLOADER == 'selenium':
            if 'proxy' in request.meta:
                self.browser = myselenium.load_firefox(load_images=False,display=True, proxy=request.meta['proxy'].decode('utf-8'))
            else:
                self.browser = myselenium.load_firefox(load_images=False, display=True)
            self.browser.get(request.url)
            res = TextResponse(url=self.browser.current_url, body=self.browser.page_source)  # page_source是纯文本形式
            self.browser.close()
            return TextResponse(url=request.url,status=200,headers=request.headers,
                                body=res.body,request=request)
