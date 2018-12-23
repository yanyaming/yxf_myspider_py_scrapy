yxf_spider_py_scrapy : 爬虫服务项目
=========================================================

## 项目开发

项目主题：通用爬虫服务框架  

开发环境：Linux（CentOS 7），python，scrapy，redis，postgresql   

编程语言：python  

IDE：Pycharm  

git根目录：yxf_myspider_py_scrapy  

爬虫根目录：yxf_myspider_py_scrapy/myspider（后面以./myspider表示）  

### 项目依赖  

python==3.6.x  

pip>=18.x  

postgresql  

yxf_myspider_py_scrapy/requirments.txt  

### 项目架构

队列存储服务器-VPS：redis  

数据存储服务器-VPS：postgresql  

爬虫管理服务器-VPS：scrapyd  

代理IP服务器-本地：IPProxyPool（在别人的项目基础上做了修改。原项目：https://github.com/qiyeboy/IPProxyPool）  

工作服务器-本地：scrapy(myspider)  

数据查询API服务器-VPS：webserver  

    前端展示服务器-VPS：mysite(http://avata.cc)

### Scrapy项目开发  

1.初始化工程:  

	进入想要放置scrapy项目的路径：
	/usr/local/python3/bin/scrapy startproject myspider——新建一个主项目，会自动生成多个文件

2.为了适应健壮性、通用性、分布式目的，将./myspider/myspider目录内修改为新的组织形式（略去init文件）:  

	settings.py——爬虫配置文件
	settings.cfg——敏感信息配置文件（克隆代码使用时需手动创建）
	redis.py——队列存储管理


### 思路

爬取逻辑：

	爬取网页由谁来执行？slaver-myspider和slaver-ipproxypool。
	重点考虑spidermiddleware和downloadermiddleware，从发起请求到收到正确网页并解析得到正确Item的过程。
	请求网页与解析中的异常处理，包括超时、错误url、反爬、验证码、解析失败等。
	尽量模仿正常访问，动态UA、代理IP、Cookies、正确的Header头部、登录账号甚至账号轮换等。

调度与存储逻辑：

	队列由谁来管理？master-redis和master-scrapyd。
	数据由谁来存储？master-postgresql。
	重点考虑item和pipeline，在item文件里定义解析规则，与数据库表中的数据对应起来，在pipeline里写存储流程。
	调度管理应当有多爬虫管理、随时启停、断点续爬、增量爬取、更新爬取功能。
	最初加入1个初始url，从爬到的网页中得到新url加入队列，全部爬完自动停止。
	先在本地缓存SQL语句（比如10个），超出后再提交到master存入数据库。

查询与展示逻辑：

	查询API服务由谁来提供？master-webserver（且设计成RESTfulAPI模式）。
	最终展现由谁来提供？mysite的爬虫子应用，前端用highcharts，直接调用master-webserver的API。

## 部署

Master——scrapyd爬虫服务，redis队列，postgresql数据库，web.py网站API服务  

Slaver——从master获取爬虫任务，解析得到结果后上传到master的数据库  

## 运行

Master作为服务在VPS全天候运行，Slaver在本地电脑通过手动运行脚本随时启动停止  
