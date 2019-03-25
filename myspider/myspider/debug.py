#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import sys
import os
import redis
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from myspider.settings import REDIS_URL,REDIS

'''
自己添加的文件，用于测试
'''

if __name__ == '__main__':
    r = redis.Redis(host=REDIS['host'], password=REDIS['password'], db=REDIS['db'])

    r.flushdb()
    # keywords = ['爬虫', 'python', 'scrapy', 'django']

    # r.delete('zhaopin_qianchengwuyou:dupefilter')
    # for i in keywords:
    #     r.lpush('zhaopin_qianchengwuyou:start_urls',
    #             'https://search.51job.com/list/080200,000000,0000,00,9,99,{0},2,1.html'.format(i))
    # execute(['scrapy','crawl','zhaopin_qianchengwuyou'])

    # r.delete('zhaopin_lagouwang:dupefilter')
    # for i in keywords:
    #     r.lpush('zhaopin_lagouwang:start_urls',
    #             'https://www.lagou.com/jobs/list_{0}?city=杭州'.format(i))
    # execute(['scrapy','crawl','zhaopin_lagouwang'])

    # r.delete('fangchan_anjuke_zufang:dupefilter')
    # r.lpush('fangchan_anjuke_zufang:start_urls', 'https://hz.zu.anjuke.com/')
    # execute(['scrapy', 'crawl', 'fangchan_anjuke_zufang'])
