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
数据库、redis、IP池、查询API都在远程；
scrapyd和爬虫测试阶段在本地，测试成功后移到远程。后续更新同理，先在本地测试，后移交到远程。
（测试与运行的区分：数据库分为myspider和myspidertest，redis分为0和1）
'''

if __name__ == '__main__':
    r = redis.Redis(host=REDIS['host'], password=REDIS['password'], db=REDIS['db'])

    # r.flushdb()

    # r.delete('zhaopin_qianchengwuyou:proxy_http')
    # r.delete('zhaopin_qianchengwuyou:proxy_https')
    r.lpush('zhaopin_qianchengwuyou:start_urls', 'https://www.51job.com/')
    execute(['scrapy','crawl','zhaopin_qianchengwuyou'])
    #
    # r.delete('fangchan_anjuke_zufang:proxy_http')
    # r.delete('fangchan_anjuke_zufang:proxy_https')
    # r.lpush('fangchan_anjuke_zufang:start_urls', 'https://hz.zu.anjuke.com/')
    # execute(['scrapy', 'crawl', 'fangchan_anjuke_zufang'])
