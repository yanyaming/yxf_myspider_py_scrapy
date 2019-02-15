#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import random
import redis
import requests
from myspider.settings import REDIS_URL,REDIS,PROXY_API,PROXY_SERVER

'''
1.从第三方API或本地IP池提取一批代理IP供爬虫使用，存储于redis。
2.每次请求都会从redis随机获取代理IP，并对此IP的使用次数、失败次数进行计数。
3.根据计数结果决定后续的请求是否换IP以及是否从redis中删除失败次数多的IP，当redis中的代理被删除殆尽时再重新提取一批。

redis常用操作：
连接——r=Redis(URL)
通用——新建r['name']，判断是否存在r.exists(name)，删除r.delete(name)
列表——左侧添加r.lpush(name,value)，通过索引重新赋值r.lset(name,index,value)，
    通过索引获取值r.lindex(name,index)，通过值删除项目r.lrem(name,count,value)（count指定删除几个），
    查询长度r.llen(name)
'''

redis_pool = redis.ConnectionPool(host=REDIS['host'], port=int(REDIS['port']), db=int(REDIS['db']),password=REDIS['password'])


#每次请求都从redis随机查询出一个代理IP，若有效代理过少则通过API更新代理数据，为每个爬虫单独维护代理池
#代理IP必须使用高匿，http/https视情况而定
def _getRandomProxy(from_where,protocol,proxy_http,proxy_https):
    r = redis.StrictRedis(connection_pool=redis_pool)
    lenth1 = r.llen(proxy_http)
    lenth2 = r.llen(proxy_https)
    prefix_http = 'http://'
    prefix_https = 'https://'
    #若代理没有了，则获取
    if lenth1 <= 1 or lenth2 <= 1:
        res1=''
        res2=''
        #从第三方API提取：返回ip:port形式的纯文本列表，\n换行
        if from_where == 'api':
            '''
            参数:      参数可选输入:
            category   0 匿名,2 高匿
            protocol   (不输入默认http),https
            area       数据原文是完整地区名，可输入国家/省份/城市，API提供者进行模糊查询
            '''
            url = PROXY_API['url']+'?tid='+PROXY_API['tid']
            res1 = requests.get(url + '&category=2&num=20&protocol=http')
            time.sleep(1)
            res2 = requests.get(url+'&category=2&num=20&protocol=https')
            for i in res1.text.split('\r\n'):
                r.lpush(proxy_http, prefix_http + i)
            for i in res2.text.split('\r\n'):
                r.lpush(proxy_https, prefix_https + i)
        #从本地IP池提取：返回列表，列表内有三项，只取前两项ip和端口
        elif from_where == 'server':
            '''
            参数:       参数可选输入:
            types	    0 高匿,1 匿名,2 透明
            protocol	0 http,1 https,2 http/https
            country     国内,国外
            area	    数据原文是完整地区名，可输入国家/省份/城市，API提供者进行模糊查询
            '''
            url = PROXY_SERVER['url']+'?'
            res1 = requests.get(url + '&count=20&types=0&protocol=0')
            time.sleep(1)
            res2 = requests.get(url + '&count=20&types=0&protocol=2')
            for i in eval(res1.text):
                r.lpush(proxy_http,prefix_http+i[0]+':'+str(i[1]))
            for i in eval(res2.text):
                r.lpush(proxy_https,prefix_https+i[0]+':'+str(i[1]))
        lenth1 = r.llen(proxy_http)
        lenth2 = r.llen(proxy_https)
    #若代理库存充足则从库中随机取
    if protocol=='http':
        item = r.lindex(proxy_http,random.randint(0,lenth1-1))
    elif protocol=='https':
        item = r.lindex(proxy_https,random.randint(0,lenth2-1))
    else:
        return None
    return item


#多次失败则移出redis
def _deleteUselessProxy(proxy,proxy_http,proxy_https):
    r = redis.StrictRedis(connection_pool=redis_pool)
    if proxy.split('://')[0] == 'http':
        r.lrem(proxy_http,1,proxy)
    elif proxy.split('://')[0] == 'https':
        r.lrem(proxy_https,1,proxy)
    print('-------------lrem:'+proxy)


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        PROXY_ENABLE=spider.settings.get('PROXY_ENABLE',False)
        PROXY_MAX_USE = spider.settings.get('PROXY_MAX_USE', 10)
        PROXY_FROM_WHERE = spider.settings.get('PROXY_FROM_WHERE', 'server')

        # 添加代理
        if PROXY_ENABLE:
            proxy_http=spider.name+':proxy_http'
            proxy_https=spider.name+':proxy_https'
            protocol = request.url.split('://')[0] #网址是http就用http代理，是https就用https代理
            # 统计使用此代理的累积次数，超过数量则换代理
            used_times = request.meta.get('proxy_used_times',0)
            # 统计使用此代理的失败次数，超过数量则删除代理
            failed_times = request.meta.get('proxy_failed_times',0)
            # 操作代理
            if 'proxy' not in request.meta or failed_times >= 3 or used_times >= PROXY_MAX_USE:
                if failed_times >= 3:
                    proxy=str(request.meta['proxy'])  # proxy是scrapy默认的代理字段
                    _deleteUselessProxy(proxy,proxy_http,proxy_https)  # 如果在当前代理下失败超过3次则删除redis代理库的本代理
                request.meta['proxy'] = _getRandomProxy(PROXY_FROM_WHERE, protocol, proxy_http, proxy_https)  # 获取代理
                request.meta['proxy_used_times'] = 0
                request.meta['proxy_failed_times'] = 0
            # 更新代理使用次数
            request.meta['proxy_used_times'] += 1
            print('-------------use proxy:'+str(request.meta['proxy']))
        else:
            pass

        return None
