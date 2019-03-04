#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

'''
本代码由主服务调用，对爬虫数据库进行查询并返回数据
'''

MYSPIDER_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'myspider')
sys.path.append(MYSPIDER_ROOT)
from myspider.privatesettings import *
