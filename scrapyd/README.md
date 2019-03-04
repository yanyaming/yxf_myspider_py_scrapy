scrapyd : API简表
=========================================================

## scrapyd服务

需提前安装scrapyd（爬虫服务器端）,scrapyd-client（项目开发端）

### 项目部署命令 

（scrapyd只支持通过addversion.json安装已编译的egg文件，若要自动编译安装需要使用scrapyd-client提供的scrapyd-deploy命令）

    /usr/local/python3/bin/scrapyd-deploy myspider -p myspider

### scrapydAPI

1、获取状态

    curl http://127.0.0.1:6800/daemonstatus.json
    { "status": "ok", "running": "0", "pending": "0", "finished": "0", "node_name": "node-name" }

2、添加项目（若不指定版本号，则自动新建一个新版本）

    （post方式，data={"project":myproject, "version":"r23", "egg":"@myproject.egg"}）
    curl http://localhost:6800/addversion.json -F project=myproject -F version=r23 -F egg=@myproject.egg
    {"status": "ok", "spiders": 3}

3、获取项目列表

    curl http://127.0.0.1:6800/listprojects.json
    {"status": "ok", "projects": ["myproject", "otherproject"]}

4、获取项目下已发布的爬虫列表

    curl http://127.0.0.1:6800/listspiders.json?project=myproject
    {"status": "ok", "spiders": ["spider1", "spider2", "spider3"]}

5、获取项目下已发布的爬虫版本列表（爬虫版本跟随项目版本，若要更新某个爬虫，则整个项目都要更新）

    curl http://127.0.0.1:6800/listversions.json?project=myproject
    {"status": "ok", "versions": ["r99", "r156"]}

6、获取爬虫运行状态

    curl http://127.0.0.1:6800/listjobs.json?project=myproject
    {"status": "ok",
     "pending": [{"id": "78391cc0fcaf11e1b0090800272a6d06", "spider": "spider1"}],
     "running": [{"id": "422e608f9f28cef127b3d5ef93fe9399", "spider": "spider2", "start_time": "2012-09-12 10:14:03.594664"}],
     "finished": [{"id": "2f16646cfcaf11e1b0090800272a6d06", "spider": "spider3", "start_time": "2012-09-12 10:14:03.594664", "end_time": "2012-09-12 10:24:03.594664"}]}

7、启动服务器上某一爬虫（必须是已发布到服务器的爬虫）

    （post方式，data={"project":"myproject", "spider":"myspider"}）
    curl http://localhost:6800/schedule.json -d project=myproject -d spider=somespider
    {"status": "ok", "jobid": "6487ec79947edab326d6db28a2d86511e8247444"}

8、停止服务器上某一爬虫（若之前是运行则结束，若之前是pending等待则取消）

    （post方式，data={"project":"myproject", "job":"6487ec79947edab326d6db28a2d86511e8247444"}）
    curl http://localhost:6800/cancel.json -d project=myproject -d job=6487ec79947edab326d6db28a2d86511e8247444
    {"status": "ok", "prevstate": "running"}

9、删除某一版本工程

    （post方式，data={"project":"myproject","version":"r99"}）
    curl http://localhost:6800/delversion.json -d project=myproject -d version=r99
    {"status": "ok"}

10、删除某一工程，包括该工程下的各版本

    （post方式，data={"project":"myproject"}）
    curl http://localhost:6800/delproject.json -d project=myproject
    {"status": "ok"}
