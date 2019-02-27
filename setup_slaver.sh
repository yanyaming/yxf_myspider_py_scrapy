#!/bin/sh
# -*- coding: utf-8 -*-
pip3 install -r requirements.txt
cd ./webdriver
unzip webdriver.zip
cp -vfR chromedrier $2
rm -vrf $1
exit 0



#old
#yum -y install docker
#systemctl enable docker
#systemctl start docker
#docker pull scrapinghub/splash
