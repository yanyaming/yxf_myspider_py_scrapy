yxf_spider_py_scrapy : 爬虫服务项目
=========================================================

------------

## 项目开发

项目主题：通用爬虫服务框架  

开发环境：Linux（CentOS 7），python，scrapy，mongodb  

编程语言：python  

git根目录：yxf_myspider_py_scrapy  

网站项目根目录：yxf_myspider_py_scrapy/myspider（后面以./myspider表示）  

与网站内容无关的环境配置脚本：yxf_myspider_py_scrapy/scripts  

### 项目依赖  

python==2.7.x  

pip>=18.x  

mongodb  

scrapy=1.5.x  

### 项目架构

管理服务器-VPS（）：docker-master

数据库服务器-VPS（提供大量非关系数据存储服务）：mongodb  

工作服务器-本地（）：scrapy，redis  

#### Scrapy项目开发  

1.初始化工程:  

	进入想要放置scrapy项目的路径：
	scrapy startproject myspider——新建一个主项目作为一个完整的爬虫框架
	目录内容：
	myspider.cfg——项目整体配置
	myspider/——项目代码
	    __init__.py
	    items.py——数据存储模型
	    middlewares.py——下载器中间件（可配置代理和会话）和爬虫中间件
	    pipelines.py——数据处理行为
	    settings.py——爬虫配置文件
	    spiders/——具体爬虫代码
	        __init__.py
	        ...(添加各种爬虫规则)

2.随着爬取网站的不同逐渐添加新子爬虫:  

	进入项目路径：
	scrapy genspider spidername domainname——新建一个子爬虫（把spidername添加到spider中）

------------

## 部署

使用Docker打包：./docker_image  

Master-Daemon1——管理爬虫服务器  
Master-Daemon2——维护urls队列  
Master-Daemon3——数据库同步管理  

Slaver-requestWork（每台机器5个线程，维护Session&Cookie，请求网页数据）  
——中间件：代理ip池，模拟登录，验证码识别，反反爬虫策略，异常处理  

Slaver-parserWork（每台机器5个线程，解析目标数据，获取url列表，存入数据库）  
——中间件：数据模型  

Slaver-dataWork（mongodb非关系数据库服务器）  

### 分布式部署

服务器主机Master——管理Docker：Vultr-VPS（ip，ssh，ftp，root），docker，建立实例，作为服务运行  

本地电脑Slaver：任意Linux系统，安装，任意时刻手动运行  

------------

## 运行
