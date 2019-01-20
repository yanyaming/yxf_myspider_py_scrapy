#!/bin/sh
# -*- coding: utf-8 -*-
pip3 install -r requirements.txt
yum -y install docker
systemctl enable docker
systemctl start docker
docker pull scrapinghub/splash
exit 0
