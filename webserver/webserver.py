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
from webserver.getdata import SqlQuery


urls = (
    '/', 'select',
    '/delete', 'delete',
    '/login', 'login',
    '/logout', 'logout',
)


def start_api_server():
    sys.argv.append('0.0.0.0:%s' % config.API_PORT)
    app = web.application(urls, globals())
    app.run()


class select(object):
    def GET(self):
        inputs = web.input()  # query:?type=1&name=admin;storage:{'type': u'1', 'name': u'admin'}
        json_result = json.dumps(sqlhelper.select(inputs.get('count', None), inputs))
        return json_result


class delete(object):
    params = {}

    def GET(self):
        inputs = web.input()
        json_result = json.dumps(sqlhelper.delete(inputs))
        return json_result


if __name__ == '__main__':
    sys.argv.append('0.0.0.0:8080')
    app = web.application(urls, globals())
    app.run()
