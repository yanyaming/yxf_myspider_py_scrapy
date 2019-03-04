#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import configparser
from myspider.privatesettings import *

'''
本代码由主服务调用，对爬虫数据库进行查询并返回数据
'''

WEB_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(WEB_ROOT)
SCRAPY_ROOT = os.path.join(os.path.dirname(WEB_ROOT),'myspider')
