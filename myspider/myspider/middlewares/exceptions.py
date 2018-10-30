#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
import traceback
from scrapy.exceptions import IgnoreRequest
import smtplib # python自带的邮件库
from email.mime.text import MIMEText # python自带的邮件库
from email.header import Header # python自带的邮件库
from myspider.settings import EMAIL

#邮件通知
def send_email():
    #login
    server = smtplib.SMTP(EMAIL["SMTPserver"], EMAIL["port"])
    server.login(EMAIL["address"], EMAIL["password"])
    #send email
    msg = MIMEText('爬虫Master被封警告！请求解封！', 'plain', 'utf-8')
    msg['From'] = EMAIL["from"]
    msg['Subject'] = Header('爬虫被封禁警告！', 'utf8').encode()
    msg['To'] = EMAIL["to"]
    server.sendmail(msg['From'], [msg['To']], msg.as_string())


class RequestFailMiddleware(object):

    def process_spider_exception(self, response, exception, spider):
        response.request.meta['proxy_failed_times'] += 1
        spider.logger.info('----------spider GET failed')
        # raise exception
        return response.request.replace(dont_filter=True)

    def process_exception(self, request, exception, spider):
        # request.meta['proxy_failed_times'] += 1
        spider.logger.info('----------downloader GET failed')
        # if request.meta['proxy_failed_times']>5:
        #     traceback.print_exc(exception)
        # return request.replace(dont_filter=True)
        raise exception

    def process_response(self, request, response, spider):
        http_code = response.status
        #1xx请求未完成，需要放行
        if http_code // 100 == 1:
            return response
        #2xx
        if http_code // 100 == 2:
            return response
        #3xx
        if http_code // 100 == 3 and http_code != 304 and http_code != 302:
            spider.logger.info('status code:'+str(http_code))
            request.meta['proxy_failed_times'] += 1
            return request.replace(dont_filter=True)
        if http_code == 304:
            request.meta['proxy_failed_times'] += 1
            spider.logger.info('status code:304')
            return response
        if http_code == 302:
            request.meta['proxy_failed_times'] += 1
            spider.logger.info('status code:302')
            return response
        #4xx
        if http_code // 100 == 4:
            spider.logger.info('status code:4xx')
            raise IgnoreRequest(str(http_code))
        #5xx
        if http_code // 100 == 5:
            request.meta['proxy_failed_times'] += 1
            spider.logger.info('status code:'+str(http_code))
            return request.replace(dont_filter=True)
