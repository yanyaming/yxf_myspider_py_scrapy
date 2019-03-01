#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import configparser

'''
本代码由主服务调用，对爬虫数据库进行查询并返回数据
'''

WEB_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(WEB_ROOT)
# SCRAPYD_ROOT = os.path.join(os.path.dirname(WEB_ROOT),'scrapyd')
SCRAPY_ROOT = os.path.join(os.path.dirname(WEB_ROOT),'myspider')

cf = configparser.ConfigParser()
cf.read(os.path.join(SCRAPY_ROOT,"settings.cfg"))
MASTER_HOST = cf.get('meta','masterhost')
MASTER = cf.getboolean('meta','master')
if MASTER:
    REDIS_URL = cf.get('redis-master','url')
    REDIS = {
        'host':cf.get('redis-master','host'),
        'port':cf.get('redis-master','port'),
        'password':cf.get('redis-master','password'),
        'db':cf.get('redis-master','db'),
    }
    DATABASE = {
        'host': cf.get('db-master', 'host'),
        'port': cf.get('db-master', 'port'),
        'user': cf.get('db-master', 'user'),
        'password': cf.get('db-master', 'password'),
        'db': cf.get('db-master', 'db'),
    }
    DATABASE_URL = cf.get('db-master','url')
else:
    REDIS_URL = cf.get('redis-slaver','url')
    REDIS = {
        'host':cf.get('redis-slaver','host'),
        'port':cf.get('redis-slaver','port'),
        'password':cf.get('redis-slaver','password'),
        'db':cf.get('redis-slaver','db'),
    }
    DATABASE = {
        'host': cf.get('db-slaver', 'host'),
        'port': cf.get('db-slaver', 'port'),
        'user': cf.get('db-slaver', 'user'),
        'password': cf.get('db-slaver', 'password'),
        'db': cf.get('db-slaver', 'db'),
    }
    DATABASE_URL = cf.get('db-slaver','url')
