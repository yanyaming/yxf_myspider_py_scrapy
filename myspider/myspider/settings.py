# -*- coding: utf-8 -*-

# Scrapy settings for myspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import ConfigParser
cf = ConfigParser.ConfigParser()
cf.read("settings.cfg")

#项目名称
BOT_NAME = 'myspider'

#项目模块
SPIDER_MODULES = ['myspider.spiders']
NEWSPIDER_MODULE = 'myspider.spiders'

#-----------------下载器配置--------------------

#固定浏览器UA
#USER_AGENT = 'myspider (+http://www.yourdomain.com)'

#服从robots.txt协议
ROBOTSTXT_OBEY = True

#抓取网站的最大允许的抓取深度值
DEPTH_LIMIT=0

#scrapy downloader并发请求最大值
#CONCURRENT_REQUESTS = 32

#对同一网站的请求时延
#DOWNLOAD_DELAY = 3

#等待响应时延
DOWNLOAD_TIMEOUT=10

#DNS域名缓存
DNSCACHE_ENABLED=True

#最高并发请求值（两个配置二选一）
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

#禁用cookie
#COOKIES_ENABLED = False

#禁用Telnet Console
#TELNETCONSOLE_ENABLED = False

#自定义请求头
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

#-----------------中间件等组件配置-------------------------

#spider中间件
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    # 'myspider.middlewares.MyspiderSpiderMiddleware': 543,
}

#downloader中间件
DOWNLOADER_MIDDLEWARES = {
    "tc_zufang.Proxy_Middleware.ProxyMiddleware":100,
    'tc_zufang.rotate_useragent_dowmloadmiddleware.RotateUserAgentMiddleware':400,
    'tc_zufang.redirect_middleware.Redirect_Middleware':500,
    # 'myspider.middlewares.MyspiderDownloaderMiddleware': 543,
}

#extensions附加组件
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

#pipelines管道
ITEM_PIPELINES = {
    'myspider.pipelines.MyspiderPipeline': 300,
}

#--------------------爬虫框架配置------------------

#自动限速
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False

#HTTP缓存
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'

#配置日志存储目录
LOG_FILE = "logs/scrapy.log"

#-------------------外部配置----------------------

Master_Server = {
    'url':cf.get('server','masterhost'),
}

MASTER = cf.getboolean('server','master')

if MASTER is True:
    QUEUE_DB = {
        'ENGINE': cf.get('queuedb-master','engine'),
        'DB': cf.get('queuedb-master','db'),
        'HOST': cf.get('queuedb-master','host'),
        'PORT': cf.get('queuedb-master','port'),
    }
else:
    QUEUE_DB = {
        'URL': cf.get('queuedb-slaver','url')
    }

NOSQL_DB = {
    'ENGINE': cf.get('nosqldb','engine'),
    'DB': cf.get('nosqldb','db'),
    'USER': cf.get('nosqldb','user'),
    'PASSWORD': cf.get('nosqldb','password'),
    'HOST': cf.get('nosqldb','host'),
    'PORT': cf.get('nosqldb','port'),
}

IP_Proxy_API = {
    'url':cf.get('proxyapi','url'),
    'orderid':cf.get('proxyapi','orderid'),
    'args':cf.get('proxyapi','args'),
}

IP_Proxy_Page = {
    'url':cf.get('proxypage','url'),
}
