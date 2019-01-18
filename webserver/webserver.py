#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import web
import sys
import json
import os
WEB_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(WEB_ROOT)
SCRAPYD_ROOT = os.path.join(os.path.dirname(WEB_ROOT),'scrapyd')
SCRAPY_ROOT = os.path.join(os.path.dirname(WEB_ROOT),'myspider')
from getdata import SqlQuery


'''
本服务将作为爬虫网站（独立域名）的默认网站服务（8080），提供网站首页和数据API接口
'''

urls = (
    '/', 'index',
    '/api', 'api',
    '/stat', 'stat',
)


class index(object):
    def GET(self):
        inputs = web.input()  # query:?type=1&name=admin;storage:{'type': u'1', 'name': u'admin'}
        json_result = json.dumps(sqlhelper.select(inputs.get('count', None), inputs))
        return json_result


class api(object):
    params = {}

    def GET(self):
        inputs = web.input()  # query:?type=1&name=admin;storage:{'type': u'1', 'name': u'admin'}
        json_result = json.dumps(sqlhelper.select(inputs.get('count', None), inputs))
        return json_result


class stat(object):
    def GET(self):
        pass


if __name__ == '__main__':
    sys.argv.append('0.0.0.0:8080')
    app = web.application(urls, globals())
    app.run()
