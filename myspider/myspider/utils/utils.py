# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # 使用py3的字符串表示法，不加u前缀也用unicode
from __future__ import print_function # 使用py3的print()函数
import os
import random
import smtplib # python自带的邮件库
from email.mime.text import MIMEText # python自带的邮件库
from email.header import Header # python自带的邮件库
import ConfigParser

#requirments
import redis
import requests

from myspider.settings import QUEUE_DB

#parse .cfg
cf = ConfigParser.ConfigParser()
cf.read(os.path.join("myspider","settings.cfg"))

def send_email():
    #login
    server = smtplib.SMTP(cf.get("email","SMTPserver"), cf.getboolean("email","port"))
    server.login(cf.get("email","address"), cf.get("email","password"))
    #send email
    msg = MIMEText('爬虫Master被封警告！请求解封！', 'plain', 'utf-8')
    msg['From'] = cf.get("email","from")
    msg['Subject'] = Header('爬虫被封禁警告！', 'utf8').encode()
    msg['To'] = cf.get("email","to")
    server.sendmail('seven_2016@163.com', ['751401459@qq.com'], msg.as_string())

def getIPs():
    pass

def redis_inserintotc(str,type):
    try:
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    except:
        print '连接redis失败'
    else:
        if type == 1:
            r.lpush('start_urls', str)
def redis_inserintota(str,type):
    try:
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    except:
        print '连接redis失败'
    else:
        if type == 2:
            r.lpush('tczufang_tc:requests', str)
