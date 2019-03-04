#!/bin/sh
# -*- coding: utf-8 -*-
echo "----------pip install--------------"
pip3 install -r requirements.txt
echo "----------unzip webdriver----------"
cd ./webdriver
unzip webdriver.zip
chmod 777 *
echo "----------deploy scrapyd-----------"
cd ..
./stop_server.sh
./start_server_slaver.sh
sleep 3
cd ./myspider
/usr/local/python3/bin/scrapyd-deploy myspider -p myspider
cd ..
./stop_server.sh
echo "----------done---------------------"
exit 0
