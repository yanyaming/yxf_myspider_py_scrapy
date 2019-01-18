#!/bin/sh

#goto project root
curpath=$(cd "$(dirname "$0")"; pwd)
cd $curpath
#config
sed -i 's/master=True/master=False/g' myspider/settings.cfg

#scrapyd
cd ./scrapyd
nohup python3 /usr/local/python3/bin/scrapyd > scrapyd.log 2>&1 &
cd ..

echo "server is running in background(slaver)"
echo "scrapyd:port=6800(public)"
exit 0
