#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import sys
import os
import redis
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from myspider.settings import REDIS_URL,REDIS

'''
自己添加的文件，用于测试。爬虫是大批量异步运行的程序，bug很难跟踪，写好测试代码非常重要
'''

if __name__ == '__main__':
    r = redis.Redis(host=REDIS['host'], password=REDIS['password'])

    # r.flushdb()

    # r.delete('fangchan_58_zufang:proxy_http')
    # r.delete('fangchan_58_zufang:proxy_https')
    # r.lpush('fangchan_58_zufang:start_urls', 'http://wx.58.com/chuzu/')
    # execute(['scrapy','crawl','fangchan_58_zufang'])
    #
    # r.delete('fangchan_fangtianxia_zufang:proxy_http')
    # r.delete('fangchan_fangtianxia_zufang:proxy_https')
    # r.lpush('fangchan_fangtianxia_zufang:start_urls', 'http://wuxi.zu.fang.com/')
    # execute(['scrapy', 'crawl', 'fangchan_fangtianxia_zufang'])
    #
    r.delete('fangchan_anjuke_zufang:proxy_http')
    r.delete('fangchan_anjuke_zufang:proxy_https')
    r.lpush('fangchan_anjuke_zufang:start_urls', 'https://wx.zu.anjuke.com/')
    execute(['scrapy', 'crawl', 'fangchan_anjuke_zufang'])
