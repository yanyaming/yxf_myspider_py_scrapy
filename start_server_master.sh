#!/bin/sh

#goto project root
curpath=$(cd "$(dirname "$0")"; pwd)
cd $curpath
#config
sed -i 's/master=False/master=True/g' myspider/settings.cfg

#scrapyd
cd ./scrapyd
nohup python3 /usr/local/python3/bin/scrapyd > scrapyd.log 2>&1 &
cd ..

#web
cd ./webserver
nohup python3 webserver.py > webserver.log 2>&1 &
cd ..

echo "server is running in background(master)"
echo "redis is already:port=6379(public)"
echo "mongodb is already:port=27017(public)"
echo "scrapyd:port=6800(public)"
echo "webserver:port=8080(public)"
exit 0
