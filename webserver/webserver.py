#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import web
import json
import redis
import pymongo
import requests
from loadenv import *


'''
本服务将作为爬虫网站（独立域名）的默认网站服务（8080），提供操作爬虫服务器的API接口
'''

urls = (
    '/', 'index',
    '/stats', 'stats',
    '/api', 'api',
)


class index(object):
    def GET(self):
        inputs = web.input()  # query:?type=1&name=admin;storage:{'type': u'1', 'name': u'admin'}
        result = {}
        json_result = json.dumps(result, ensure_ascii=False)
        return json_result


class stats(object):
    def GET(self):
        inputs = web.input()
        r = redis.StrictRedis(host=REDIS['host'], port=int(REDIS['port']), db=int(REDIS['db']),password=REDIS['password'])
        m_client = pymongo.MongoClient(DATABASE_URL)
        m_db = m_client[DATABASE['db']]
        result = {'redis': [], 'mongodb': [], 'crawler': []}
        spiders = set()

        for k in r.keys('*'):
            r_query_k = str(k, encoding='utf-8')
            if r_query_k != 'crawler':
                spiders.add(r_query_k.split(':')[0])
            r_query_type = str(r.type(k), encoding='utf-8')
            if r_query_k != 'crawler':
                if r_query_k.split(':')[1] == 'dupefilter':
                    r_query_count = str(r.scard(k))
                    r_query_example = str(r.srandmember(k,1)[0],encoding='utf-8')
                elif r_query_k.split(':')[1] == 'requests':
                    r_query_count = str(r.zcard(k))
                    r_query_example = str(r.zrange(k,0,1000)[0])
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
            elif r_query_k == 'crawler':
                for k in r.hgetall(b'crawler'):
                    result['crawler'].append({str(k,encoding='utf-8'): str(r.hget(b'crawler',k),encoding='utf-8')})

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
        return json_result


class api(object):
    params = {}

    def GET(self):
        inputs = web.input()
        r = redis.StrictRedis(host=REDIS['host'], port=int(REDIS['port']), db=int(REDIS['db']),password=REDIS['password'])

        result = {}
        if inputs.get('op', None) == 'addurl':
            spidername = inputs.get('spidername',None)
            url = inputs.get('url',None)
            if spidername and url:
                r.lpush(spidername+':start_urls', url)
                result['status'] = 'ok'
            else:
                result['status'] = 'error'
        elif inputs.get('op', None) == 'flush':
            spidername = inputs.get('spidername', None)
            if spidername:
                r.delete(spidername+':dupefilter')
                result['status'] = 'ok'
            else:
                result['status'] = 'error'
        else:
            pass
        json_result = json.dumps(result, ensure_ascii=False)
        return json_result


if __name__ == '__main__':
    sys.argv.append('0.0.0.0:8080')
    app = web.application(urls, globals())
    app.run()
