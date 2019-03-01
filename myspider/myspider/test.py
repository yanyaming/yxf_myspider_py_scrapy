#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import sys
import os
import requests
import redis
import pymongo
import json
import time
from myspider.downloaders import myselenium
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from myspider.settings import REDIS,REDIS_URL,DATABASE,DATABASE_URL

if __name__ == '__main__':
    r = redis.StrictRedis(host=REDIS['host'], port=int(REDIS['port']), db=int(REDIS['db']), password=REDIS['password'])
    m_client = pymongo.MongoClient(DATABASE_URL)
    m_db = m_client[DATABASE['db']]

    result = {'redis': [], 'mongodb': []}
    spiders = set()

    for k in r.keys('*'):
        r_query_k = str(k, encoding='utf-8')
        spiders.add(r_query_k.split(':')[0])
        r_query_type = str(r.type(k), encoding='utf-8')
        if r_query_k.split(':')[1] == 'dupefilter':
            r_query_count = str(r.scard(k))
            r_query_example = str(r.srandmember(k, 1)[0],encoding='utf-8')
        else:
            r_query_count = str(r.llen(k))
            r_query_example = str(r.lrange(k, 0, 0)[0],encoding='utf-8')
        result['redis'].append({
            r_query_k: {
                'type': r_query_type,
                'count': r_query_count,
                'example': r_query_example,
            }
        })

    for s in spiders:
        m_co = m_db[s]
        m_query_count = str(m_co.count())
        m_query_one = m_co.find()[0]
        m_query_one['_id'] = str(m_query_one['_id'])
        m_query_one['crawl_time'] = str(m_query_one['crawl_time'])
        result['mongodb'].append({
            s: {
                'count': m_query_count,
                'example': m_query_one,
            }
        })

    json_result = json.dumps(result, ensure_ascii=False)
    print(result)
    print(json_result)
