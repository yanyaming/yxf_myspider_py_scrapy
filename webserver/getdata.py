#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import configparser
import psycopg2
import psycopg2.pool

'''
本代码由主服务调用，对爬虫数据库进行查询并返回数据
'''

WEB_ROOT = os.path.dirname(os.path.abspath(__file__))
SCRAPYD_ROOT = os.path.join(os.path.dirname(WEB_ROOT),'scrapyd')
SCRAPY_ROOT = os.path.join(os.path.dirname(WEB_ROOT),'myspider')

cf = configparser.ConfigParser()
cf.read(os.path.join(SCRAPY_ROOT,"settings.cfg"))
DATABASE = {
    'host': cf.get('db-slaver', 'host'),
    'port': cf.get('db-slaver', 'port'),
    'user': cf.get('db-slaver', 'user'),
    'password': cf.get('db-slaver', 'password'),
    'db': cf.get('db-slaver', 'db'),
}
CONN = ''

class SqlQuery:
    pass
