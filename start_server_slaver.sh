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

echo "server is running in background(slaver)"
echo "ipproxypool:port=8001(public)"
echo "scrapyd:port=6800(public)"
echo "webserver:port=8080(public)"
exit 0
