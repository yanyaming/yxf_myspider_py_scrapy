#!/bin/sh

#goto project root
curpath=$(cd "$(dirname "$0")"; pwd)
cd $curpath
#config
sed -i 's/MASTER = False/MASTER = True/g' myspider/myspider/privatesettings.py

#web
cd ./webserver
nohup python3 webserver.py > webserver.log 2>&1 &
cd ..

echo "server is running in background(master)"
echo "redis is already:port=6379(public)"
echo "mongodb is already:port=27017(public)"
echo "webserver:port=8080(public)"
exit 0
