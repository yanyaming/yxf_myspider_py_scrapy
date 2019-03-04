#!/bin/sh

#goto project root
curpath=$(cd "$(dirname "$0")"; pwd)
cd $curpath
#config
sed -i 's/master = False/master = True/g' myspider/myspider/privatesettings.py

#ipproxypool
cd ./IPProxyPool
nohup python3 IPProxy.py > ipproxypool.log 2>&1 &
cd ..

#scrapyd
cd ./scrapyd
nohup python3 /usr/local/python3/bin/scrapyd > scrapyd.log 2>&1 &
cd ..

#web
cd ./webserver
nohup python3 webserver.py > webserver.log 2>&1 &
cd ..

#spiderkeeper
cd ./spiderkeeper
nohup python3 /usr/local/python3/bin/spiderkeeper --database-url=sqlite:////opt/yxf_myspider_py_scrapy/spiderkeeper/SpiderKeeper.db --server=http://localhost:6800 > spiderkeeper.log 2>&1 &
cd ..

echo "server is running in background(slaver)"
echo "scrapyd:port=6800(local)"
echo "ipproxypool:port=8001(public)"
echo "webserver:port=8080(public)"
echo "spiderkeeper:port=5000(public)"
exit 0
