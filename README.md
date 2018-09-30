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

./myspider/requirments.txt  
——scrapy==2.x    
——html5lib  
——lxml  
——requests  
——bs4  

### 项目架构

管理服务器-VPS（）：docker-master

数据库服务器-VPS（提供大量非关系数据存储服务）：mongodb  

工作服务器-本地（）：scrapy，redis  

#### 爬虫架构  

Master-Daemon1——管理爬虫服务器  
Master-Daemon2——维护urls队列  
Master-Daemon3——数据库同步管理  

Slaver-requestWork（每台机器5个线程，维护Session&Cookie，请求网页数据）  
——中间件：代理ip池，模拟登录，验证码识别，反反爬虫策略，异常处理  

Slaver-parserWork（每台机器5个线程，解析目标数据，获取url列表，存入数据库）  
——中间件：数据模型  

Slaver-dataWork（mongodb非关系数据库服务器）

------------

## 部署

使用Docker打包：./docker_image  

### 分布式部署

服务器主机Master——管理Docker：Vultr-VPS（ip，ssh，ftp，root），docker，建立实例，作为服务运行  

本地电脑Slaver：任意Linux系统，安装  

------------

## 运行
