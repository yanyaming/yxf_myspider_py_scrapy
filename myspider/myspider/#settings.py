#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import configparser
cf = configparser.ConfigParser()
cf.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"settings.cfg"))

#项目名称
BOT_NAME = 'myspider'
#项目模块
SPIDER_MODULES = ['myspider.spiders']
NEWSPIDER_MODULE = 'myspider.spiders'
#代码模板路径，使用startproject命令创建新项目时使用
#TEMPLATES_DIR='templates'

#-----------------速率配置--------------------

#自动限速
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 30
#对同一网站的并发请求
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1
#AUTOTHROTTLE_DEBUG = False

#Twisted线程池
#REACTOR_THREADPOOL_MAXSIZE=10

#最大并发数据项目
#CONCURRENT_ITEMS=100
#最大并发请求
#CONCURRENT_REQUESTS = 16
#对同一网站的最大并发请求
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#对同一网站的最大并发请求（0值不限制，非0则覆盖_DOMAIN）
#CONCURRENT_REQUESTS_PER_IP = 0

#等待响应时延
#DOWNLOAD_TIMEOUT=180
#对同一网站的请求间隔
#DOWNLOAD_DELAY = 0
#随机请求间隔（DOWNLOAD_DELAY*0.5~1.5）
#RANDOMIZE_DOWNLOAD_DELAY=True
#最大下载大小
#DOWNLOAD_MAXSIZE=1073741824
#开始警告的大小
#DOWNLOAD_WARNSIZE=33554432#32MB

#请求超时失败或返回特定响应码的重试
#ETRY_ENABLED=True
#最多重试次数
#RETRY_TIMES=2
#RETRY_HTTP_CODES=[500, 502, 503, 504, 408]
#调整优先级
#RETRY_PRIORITY_ADJUST=-1

#重定向
#REDIRECT_ENABLED=True
#METAREFRESH_ENABLED=True
#最大重定向次数（避免死循环）
#REDIRECT_MAX_TIMES=20
#调整优先级
#REDIRECT_PRIORITY_ADJUST=+2

#-----------------爬取功能配置--------------------

#自定义请求头
#DEFAULT_REQUEST_HEADERS = {
#    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#    'Accept-Language': 'en',
#    'Accept-Encoding': 'gzip, deflate',
#}
#固定浏览器UA
#USER_AGENT = 'myspider (+http://www.yourdomain.com)'

#robots.txt协议
#ROBOTSTXT_OBEY = True

#抓取网站的最大允许的抓取深度值（0值不限制）
#DEPTH_LIMIT=0
#抓取优先级调整（正值广度优先遍历，负值深度优先遍历）
#DEPTH_PRIORITY=0
#收集最大深度信息
#DEPTH_STATS=True
#每个请求都添加深度信息
#DEPTH_STATS_VERBOSE=False

#允许抓取的网址的最大网址长度
#URLLENGTH_LIMIT=2083

#cookie
#COOKIES_ENABLED = True

#启用AJAX抓取
#AJAXCRAWL_ENABLED = True

#启用代理（启用ProxyMiddleware）
#HTTPPROXY_ENABLED=True

#在请求中加入来源地址
#REFERER_ENABLED=True

#爬取FTP的设置
#使用被动模式
#FTP_PASSIVE_MODE=True
#FTP_PASSWORD="guest"
#FTP_USER="anonymous"

#--------------------爬虫框架功能配置------------------

#HTTP缓存
#HTTPCACHE_ENABLED = False

#DNS域名缓存
#DNSCACHE_ENABLED=True

#允许压缩传输（gzip,deflate）
#COMPRESSION_ENABLED=True

#收集下载器信息
#DOWNLOADER_STATS=True

#日志级别
#LOG_LEVEL='DEBUG'
#把所有标准输出重定向到日志
#LOG_STDOUT=False
#配置日志存储目录
#LOG_FILE = "logs/scrapy.log"

#Telnet控制台
#TELNETCONSOLE_ENABLED = True
#TELNETCONSOLE_PORT=[6023, 6073]

#内存监控
#MEMUSAGE_ENABLED=True
#内存检查时间间隔
#MEMUSAGE_CHECK_INTERVAL_SECONDS=60
#最大警告内存（比MEMUSAGE_LIMIT_MB小，超出则发送警告邮件，再超出则自动杀死进程）
#MEMUSAGE_WARNING_MB=0
#内存超限邮件通知
#MEMUSAGE_NOTIFY_MAIL=False#e.g.['user@example.com']
#限制最大内存，超出则自动关闭爬虫
#MEMUSAGE_LIMIT_MB=0

#-----------------scrapy_redis配置(详见https://github.com/rmax/scrapy-redis)-------------------------

# Enables scheduling storing requests queue in redis.
#SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
#DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Default requests serializer is pickle, but it can be changed to any module
# with loads and dumps functions. Note that pickle is not compatible between
# python versions.
# Caveat: In python 3.x, the serializer must return strings keys and support
# bytes as values. Because of this reason the json or msgpack module will not
# work by default. In python 2.x there is no such issue and you can use
# 'json' or 'msgpack' as serializers.
#SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"

# Don't cleanup redis queues, allows to pause/resume crawls.
#SCHEDULER_PERSIST = True

# Schedule requests using a priority queue. (default)
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'

# Alternative queues.
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# Max idle time to prevent the spider from being closed when distributed crawling.
# This only works if queue class is SpiderQueue or SpiderStack,
# and may also block the same time when your spider start at the first time (because the queue is empty).
#SCHEDULER_IDLE_BEFORE_CLOSE = 10

# Store scraped item in redis for post-processing.
#ITEM_PIPELINES = {
#    'scrapy_redis.pipelines.RedisPipeline': 300
#}

# The item pipeline serializes and stores the items in this redis key.
#REDIS_ITEMS_KEY = '%(spider)s:items'

# The items serializer is by default ScrapyJSONEncoder. You can use any
# importable path to a callable object.
#REDIS_ITEMS_SERIALIZER = 'json.dumps'

# Specify the host and port to use when connecting to Redis (optional).
#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379

# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
#REDIS_URL = 'redis://user:pass@hostname:9001'

# Custom redis client parameters (i.e.: socket timeout, etc.)
#REDIS_PARAMS  = {}
# Use custom redis client class.
#REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

# If True, it uses redis' ``SPOP`` operation. You have to use the ``SADD``
# command to add URLs to the redis queue. This could be useful if you
# want to avoid duplicates in your start urls list and the order of
# processing does not matter.
#REDIS_START_URLS_AS_SET = False

# Default start urls key for RedisSpider and RedisCrawlSpider.
#REDIS_START_URLS_KEY = '%(name)s:start_urls'

# Use other encoding than utf-8 for redis.
#REDIS_ENCODING = 'latin1'

#-----------------中间件等组件配置-------------------------

#spider中间件
# SPIDER_MIDDLEWARES = {
#     #BASE
#     #过滤掉不成功的请求（最好关闭，反爬措施会采取httpcode欺骗）
#     'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
#     #过滤掉对其他域名的请求
#     'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
#     #在下次的请求中添加请求头信息：referer引用来源
#     'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
#     #过滤url超过限制长度的请求
#     'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
#     #设置爬取深度信息以及深度限制
#     'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
# }

#downloader中间件
# DOWNLOADER_MIDDLEWARES = {
#     #BASE
#     #robots.txt协议,不爬取Disallow规定禁止爬取的URL
#     'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
#     #http基本身份认证,http://user:pass@domain.com,把用户名密码加密后的数据放入请求头
#     'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
#     #载入settings里的超时配置项
#     'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
#     #载入settings里的默认请求头
#     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
#     #载入settings里的默认UA
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
#     #请求失败重试
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
#     #爬取ajax,框架会自动爬取形如http://example.com/!#foo=bar的AJAX页面
#     #此中间件在原网址中添加#!,用于爬取没有!#的AJAX页面
#     'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
#     #处理head重定向,<meta http-equiv="refresh" content="[timedelay]"; url="[newpage]">
#     'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
#     #处理压缩传输
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
#     #处理body重定向
#     'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
#     #Cookie,CookieJar:对每个域名、每个爬虫单独设置（需要在每个爬虫代码里显式传递）
#     'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
#     #网络代理,在Request对象的meta信息中加入代理信息，通过代理访问,http_proxy/https_proxy
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
#     #状态信息
#     'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
#     #HTTP缓存
#     'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
# }

#pipelines管道
# ITEM_PIPELINES = {
#     #REDIS
#     'scrapy_redis.pipelines.RedisPipeline': 300,
# }

#下载处理
# DOWNLOAD_HANDLERS = {
#     'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
#     'http': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
#     'https': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
#     's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
#     'ftp': 'scrapy.core.downloader.handlers.ftp.FTPDownloadHandler',
# }

#extensions附加组件
# EXTENSIONS = {
#     'scrapy.extensions.corestats.CoreStats': 0,
#     'scrapy.extensions.telnet.TelnetConsole': 0,
#     'scrapy.extensions.memusage.MemoryUsage': 0,
#     'scrapy.extensions.memdebug.MemoryDebugger': 0,
#     'scrapy.extensions.closespider.CloseSpider': 0,
#     'scrapy.extensions.feedexport.FeedExporter': 0,
#     'scrapy.extensions.logstats.LogStats': 0,
#     'scrapy.extensions.spiderstate.SpiderState': 0,
#     'scrapy.extensions.throttle.AutoThrottle': 0,
# }

#-------------------外部配置----------------------

