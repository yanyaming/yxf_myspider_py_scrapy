yxf_spider_py_scrapy : 爬虫服务项目
=========================================================

## 项目开发

项目主题：通用爬虫服务框架  

开发环境：Linux(CentOS7)  

编程语言：python  

IDE：Pycharm  

git根目录：yxf_myspider_py_scrapy  

爬虫根目录：yxf_myspider_py_scrapy/myspider（后面以./myspider表示）  

### 项目依赖  

python==3.6.x  

pip>=18.x  

mongodb  

redis  

yxf_myspider_py_scrapy/requirments.txt  

### 项目架构

主（Master）  

分布式队列存储服务器-VPS：redis([http://iotec.cc:6379])  

非关系数据存储服务器-VPS：mongodb([http://iotec.cc:27017])  

管理API服务器-VPS：webserver([http://iotec.cc:8080])  

前端网站-VPS：mysite([http://avata.cc])  

从（Slave）  

代理IP服务器-本地：IPProxyPool([http://localhost:8001]) （别人的原项目：[https://github.com/qiyeboy/IPProxyPool]）  

爬虫工作服务器-本地：scrapyd(scrapy-myspider) ([http://localhost:6800])  

爬虫管理服务器-本地：spiderkeeper([http://localhost:5000])  

搜索引擎服务器-本地（因性能问题，无法放到远程）：elasticsearch([http://localhost:9200])  

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

### BUG汇总

selenium加载webdriver-chromedriver时，找不到可执行文件？  

    chrome需要再安装浏览器，而centos下的chrome浏览器需要许多依赖，不好安装，弃用。  
    
selenium加载webdriver-firefoxdriver时，"connection refused"？  

    首先检查firefox的driver文件是否有足够权限，然后检查firefox浏览器的版本是否足够高，升级版本。  

selenium加载webdriver-firefoxdriver时，"Tried to run command without establishing a connection"？  

    不能在爬取过程中关闭引擎，可设置在爬虫的关闭事件里关闭引擎。  

爬虫中断运行时当前未完成的请求丢失？  

    采用外部下载器的代码用try-except抛出DontCloseSpider异常，然后在异常处理代码中统一重新发出请求。
    但单个爬虫实例请求队列只有一条单线，很容易宕机，可使用scrapyd同时运行多个爬虫实例，多流水线爬取。

## 部署与运行

Master在VPS全天候运行，Slaver在本地电脑通过手动运行脚本随时启动停止  
