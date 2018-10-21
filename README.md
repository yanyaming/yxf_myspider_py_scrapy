yxf_spider_py_scrapy : 爬虫服务项目
=========================================================

------------

## 项目开发

项目主题：通用爬虫服务框架  

开发环境：Linux（CentOS 7），python，scrapy，mongodb, redis, docker  

编程语言：python  

git根目录：yxf_myspider_py_scrapy  

爬虫项目根目录：yxf_myspider_py_scrapy/myspider（后面以./myspider表示）  

与爬虫内容无关的环境配置脚本：yxf_myspider_py_scrapy/scripts  

部署docker容器相关：yxf_myspider_py_scrapy/docker  

### 项目依赖  

python==2.7.x  

pip>=18.x  

mongodb  

yxf_myspider_py_scrapy/requirments  

### 项目架构

管理服务器-VPS：docker-master  

数据存储服务器-VPS：mongodb  

队列存储服务器-分布式：redis  

工作服务器-本地：scrapy  

#### Scrapy项目开发  

1.初始化工程:  

	进入想要放置scrapy项目的路径：
	scrapy startproject myspider——新建一个主项目，会自动生成多个文件

2.出于分布式和爬取多种网站架构的目的，手动将./myspider/myspider目录内修改为新的组织形式（略去init文件）:  

	settings.py——爬虫配置文件
	settings.cfg——敏感信息配置文件（克隆代码使用时需手动创建）
	redis.py——队列存储管理
	mongodb.py——数据存储管理
	abstract_items.py——数据存储模型抽象类
	abstract_pipelines.py——数据处理行为抽象类
	abstract_middlewares/——中间件抽象类
	    abstract_agent.py——模拟浏览器行为
	    abstract_selenium.py——模拟浏览器
	    abstract_proxy.py——网络代理
	    abstract_session.py——会话&Cookie维护
	    abstract_exception.py——异常处理
	    abstract_login.py——破解登录
	    abstract_capcha.py——破解验证码
	    ...
	abstract_downloader/——下载器抽象类（实际上下载器及其中间件才是重点和难点）
	    abstract_listpage_downloader.py
	    abstract_detailpage_downloader.py
	    abstract_ajaxlistpage_downloader.py
	    ...
	abstract_spiders/——爬虫抽象类
	    abstract_listpage_spider.py
	    abstract_detailpage_spider.py
	    ...
	domain1/——对应不同网站对象的爬虫实现代码
	    master_downloader.py
	    slaver_downloader.py
	    master_spider.py
	    slaver_spider.py
	    middleware/
	        agent.py
	        proxy.py
	        ...
	    items.py
	    pipelines.py
	    ...

	├── abstract_items.py
	├── abstract_middlewares
	│   └── middlewares.py
	├── abstract_pipelines.py
	├── abstract_spiders
	│   ├── a51job.py
	│   ├── anjuke.py
	│   └── __init__.py
	├── __init__.py
	├── settings_cfg.py
	└── settings.py



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
