#!/bin/sh
#goto projectroot:myspider
curpath=$(cd "$(dirname "$0")"; pwd)
cd $curpath
cd ./myspider
#ipproxypool
nohup python3 ../IPProxyPool/IPProxy.py > ./logs/ipproxypool.log 2>&1 &
#scrapyd
nohup python3 /usr/local/python3/bin/scrapyd > ./logs/scrapyd.log 2>&1 &
echo "server is running in background."
echo "ipproxypoo:port=8001"
echo "scrapyd:port=6800"
exit 0
