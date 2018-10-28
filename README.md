yxf_spider_py_scrapy : 爬虫服务项目
=========================================================

------------

## 项目开发

项目主题：通用爬虫服务框架  

开发环境：Linux（CentOS 7），python，scrapy，mongodb, redis  

编程语言：python  

IDE：Pycharm  

git根目录：yxf_myspider_py_scrapy  

爬虫项目根目录：yxf_myspider_py_scrapy/myspider（后面以./myspider表示）  

与爬虫内容无关的环境配置脚本：yxf_myspider_py_scrapy/scripts  

部署docker容器相关：yxf_myspider_py_scrapy/docker  

### 项目依赖  

python==3.6.x  

pip>=18.x  

mongodb  

yxf_myspider_py_scrapy/requirments.txt  

### 项目架构

管理服务器-VPS：scrapyd-master  

数据存储服务器-VPS：mongodb  

队列存储服务器-VPS：redis  

工作服务器-本地：scrapy  

#### Scrapy项目开发  

1.初始化工程:  

	进入想要放置scrapy项目的路径：
	/usr/local/python3/bin/scrapy startproject myspider——新建一个主项目，会自动生成多个文件

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

	├── __init__.py
	├── settings_cfg.py
	└── settings.py



------------

## 部署

Master——scrapyd爬虫服务，redis队列，mongodb数据库，django爬虫网站API服务  

Slaver——从master获取爬虫任务，解析得到结果后上传到master的数据库  

------------

## 运行
