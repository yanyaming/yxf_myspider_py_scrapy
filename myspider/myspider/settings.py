#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import configparser
cf = configparser.ConfigParser()
cf.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"settings.cfg"))

# 项目名称
BOT_NAME = 'myspider'
# 项目模块
SPIDER_MODULES = ['myspider.spiders']
NEWSPIDER_MODULE = 'myspider.spiders'
BASE_DIR = '/opt/yxf_myspider_py_scrapy'
# 代码模板路径，使用startproject命令创建新项目时使用
# TEMPLATES_DIR='templates'

# -----------------速率配置--------------------

#自动限速（是约数，不是确数，还需后面硬性规定）
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 30
#对同一网站的并发请求
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1

#最大并发数据项目
#CONCURRENT_ITEMS=100
#最大并发请求
#CONCURRENT_REQUESTS = 16
#对同一网站的最大并发请求（使用代理可并发，非代理一定不能并发）
CONCURRENT_REQUESTS_PER_DOMAIN = 1

#等待响应时延
DOWNLOAD_TIMEOUT=5#180
#对同一网站的请求间隔
DOWNLOAD_DELAY = 2#0
#随机请求间隔（DOWNLOAD_DELAY*0.5~1.5）
RANDOMIZE_DOWNLOAD_DELAY=True

#请求超时失败或返回特定响应码的重试
RETRY_ENABLED=False#True
#最多重试次数
#RETRY_TIMES=2
#RETRY_HTTP_CODES=[500, 502, 503, 504, 408]
#调整优先级
#RETRY_PRIORITY_ADJUST=-1

#重定向
REDIRECT_ENABLED=False#True

# -----------------功能配置--------------------

#预定义请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',#'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
}

#cookie
#COOKIES_ENABLED = False#True，如果不禁用会使用默认header

#robots.txt协议
ROBOTSTXT_OBEY = False#True,此处不遵守robots协议

#抓取网站的最大允许的抓取深度值（0值不限制）
#DEPTH_LIMIT=0
#抓取优先级调整（正值广度优先遍历，负值深度优先遍历）
#DEPTH_PRIORITY=0
#收集最大深度信息
#DEPTH_STATS=True
#每个请求都添加深度信息
#DEPTH_STATS_VERBOSE=False

#在请求中加入来源地址
#REFERER_ENABLED=True

#日志级别
#LOG_LEVEL='DEBUG'
#把所有标准输出重定向到日志
#LOG_STDOUT=False
#配置日志存储目录
#LOG_FILE = "logs/scrapy.log"

#内存监控
#MEMUSAGE_ENABLED=True
#最大警告内存（比MEMUSAGE_LIMIT_MB小，超出则发送警告邮件，再超出则自动杀死进程）
#MEMUSAGE_WARNING_MB=0
#内存超限邮件通知
#MEMUSAGE_NOTIFY_MAIL=False#e.g.['user@example.com']
#限制最大内存，超出则自动关闭爬虫
#MEMUSAGE_LIMIT_MB=0

# -----------------中间件等组件配置-------------------------

SCHEDULER_PERSIST = True#持久化（关闭后可保存到磁盘，重启重新加载）

SCHEDULER = "scrapy_redis.scheduler.Scheduler"#基于redis的调度器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"#基于redis的url去重类
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'#基于redis的优先级队列

# spider中间件
SPIDER_MIDDLEWARES = {
    #SCRAPY
    #过滤掉不成功的请求（最好关闭，反爬措施会采取httpcode欺骗）
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': None,#50,禁用
    #过滤掉对其他域名的请求
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
    #在下次的请求中添加请求头信息：referer引用来源
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
    #过滤url超过限制长度的请求
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
    #设置爬取深度信息以及深度限制
    'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
}

# downloader中间件
DOWNLOADER_MIDDLEWARES = {
    #SCRAPY
    #robots.txt协议,不爬取Disallow规定禁止爬取的URL
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': None,#100,禁用
    #http基本身份认证,http://user:pass@domain.com,把用户名密码加密后的数据放入请求头
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    #载入settings里的超时配置
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': None,#350,禁用
    #载入settings里的预定义请求头
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
    #载入settings里的默认UA
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,#500,重写
    #请求失败重试
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,#550,禁用
    #爬取ajax,在原网址中添加#!,用于爬取没有!#的AJAX页面
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    #处理head重定向
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': None,#580,禁用
    #处理压缩传输
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': None,#590,与requests冲突，需要单独配置
    #处理body重定向
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,#600,禁用
    #Cookie,CookieJar:对每个域名、每个爬虫单独设置（需要在每个爬虫代码里显式传递）
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    #网络代理,在Request对象的meta信息中加入代理信息，通过代理访问,http_proxy/https_proxy
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,#750,重写
    #状态信息
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    #HTTP缓存
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,

    #CUSTOM
    #动态UA
    'myspider.middlewares.myheader.MyHeaderMiddleware': 500,
    #代理
    'myspider.middlewares.myproxy.MyProxyMiddleware': 750,
    #自己选择下载器
    'myspider.middlewares.mydownloader.MyDownloaderMiddleware': 755,
    #异常处理
    'myspider.middlewares.myhandler.MyHandlerMiddleware': 760,
}

# pipelines管道
ITEM_PIPELINES = {
    #REDIS
    #REDIS任务队列管理相关
    'scrapy_redis.pipelines.RedisPipeline': 300,

    #CUSTOM
    'myspider.pipelines.mysave.MySavePipeline': 900,
}

# -------------------外部配置----------------------

MASTER_HOST = cf.get('meta','masterhost')
MASTER = cf.getboolean('meta','master')

# REDIS_URL恰好也是scrapy-redis的默认设置名称，爬虫启动后自动连接
if MASTER:
    REDIS_URL = cf.get('redis-master','url')
    REDIS = {
        'host':cf.get('redis-master','host'),
        'port':cf.get('redis-master','port'),
        'password':cf.get('redis-master','password'),
        'db':cf.get('redis-master','db'),
    }
    DATABASE = {
        'host': cf.get('db-master', 'host'),
        'port': cf.get('db-master', 'port'),
        'user': cf.get('db-master', 'user'),
        'password': cf.get('db-master', 'password'),
        'db': cf.get('db-master', 'db'),
    }
    DATABASE_URL = cf.get('db-master','url')
else:
    REDIS_URL = cf.get('redis-slaver','url')
    REDIS = {
        'host':cf.get('redis-slaver','host'),
        'port':cf.get('redis-slaver','port'),
        'password':cf.get('redis-slaver','password'),
        'db':cf.get('redis-slaver','db'),
    }
    DATABASE = {
        'host': cf.get('db-slaver', 'host'),
        'port': cf.get('db-slaver', 'port'),
        'user': cf.get('db-slaver', 'user'),
        'password': cf.get('db-slaver', 'password'),
        'db': cf.get('db-slaver', 'db'),
    }
    DATABASE_URL = cf.get('db-slaver','url')

PROXY_API = {
    'url':cf.get('proxyapi','url'),
    'tid':cf.get('proxyapi','tid'),
}

PROXY_SERVER = {
    'url':cf.get('proxyserver','url'),
}

EMAIL = {
    'SMTPserver':cf.get("email","SMTPserver"),
    'port':cf.getint("email","port"),
    'address':cf.get("email","address"),
    'password':cf.get("email","password"),
    'from':cf.get("email","from"),
    'to':cf.get("email","to"),
}
