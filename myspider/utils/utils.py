#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import random
import smtplib # python自带的邮件库
from email.mime.text import MIMEText # python自带的邮件库
from email.header import Header # python自带的邮件库
import time

#requirments
import redis
import requests
from myspider.settings import REDIS_URL,REDIS,EMAIL,PROXY_API,PROXY_SERVER

'''
redis常用操作：
连接——r=Redis(URL)
通用——新建r['name']，判断是否存在r.exists(name)，删除r.delete(name)
列表——左侧添加r.lpush(name,value)，通过索引重新赋值r.lset(name,index,value)，
    通过索引获取值r.lindex(name,index)，通过值删除项目r.lrem(name,count,value)（count指定删除几个），
    查询长度r.llen(name)
'''


#每次请求都从redis随机查询出一个代理IP，若有效代理过少则通过API更新代理数据
def getProxy(from_where='api',protocol='https'):
    r = redis.Redis(host=REDIS['host'],password=REDIS['password'])
    print(r.llen('fangchan_anjuke_zufang:start_urls'))
    lenth1 = r.llen('proxy:httpips')
    lenth2 = r.llen('proxy:httpsips')
    prefix_http = 'http://'
    prefix_https = 'https://'
    #若代理没有了，则访问API获取，返回ip:port形式的纯文本列表，\n换行
    if lenth1 <= 1 or lenth2 <= 1:
        if from_where == 'api':
            url = PROXY_API['url']+'?tid='+PROXY_API['tid']
        else:
            url = PROXY_SERVER['url']
        res1 = requests.get(url+'&category=2&num=20&protocol=http')
        for i in res1.text.split('\n'):
            r.lpush('proxy:httpips',prefix_http+i+'|5')#标记，五次失败机会
        time.sleep(1)
        res2 = requests.get(url+'&category=2&num=20&protocol=https')
        for i in res2.text.split('\n'):
            r.lpush('proxy:httpsips',prefix_https+i+'|5')
        lenth1 = r.llen('proxy:httpips')
        lenth2 = r.llen('proxy:httpsips')
    #若代理库存充足则从库中随机取
    if protocol=='http':
        item = r.lindex('proxy:httpips',random.randint(0,lenth1-1))
    elif protocol=='https':
        item = r.lindex('proxy:httpsips',random.randint(0,lenth2-1))
    else:
        return None
    return item.split('|')[0]

#统计各代理IP的失败次数，多次失败则移出redis
def anaProxy(proxy,success):
    r = redis.Redis(host=REDIS['host'],password=REDIS['password'])
    if success:
        return
    else:
        if proxy.split('/')[0] == 'http:':
            r.lrem('proxy:httpips',1,proxy)
        else:
            r.lrem('proxy:httpsips',1,proxy)
        flag=int(proxy.split('|')[1]-1)
        if flag <=0:
            return
        else:
            if proxy.split('/')[0] == 'http:':
                r.lpush('proxy:httpips',1,proxy.split('|')[0]+str(flag))
            else:
                r.lpush('proxy:httpsips',1,proxy.split('|')[0]+str(flag))


#邮件通知
def send_email():
    #login
    server = smtplib.SMTP(EMAIL["SMTPserver"], EMAIL["port"])
    server.login(EMAIL["address"], EMAIL["password"])
    #send email
    msg = MIMEText('爬虫Master被封警告！请求解封！', 'plain', 'utf-8')
    msg['From'] = EMAIL["from"]
    msg['Subject'] = Header('爬虫被封禁警告！', 'utf8').encode()
    msg['To'] = EMAIL["to"]
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
