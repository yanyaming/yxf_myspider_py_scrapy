#!/bin/sh
#CentOS
#update software lib
sudo yum -y install epel-release &&
sudo yum makecache &&
sudo yum -y install gcc &&
sudo yum -y install net-tools &&
sudo yum -y install tree &&
#install pip
sudo yum -y install python-pip &&
pip install --upgrade pip &&
pip install setuptools &&
echo "python version in this CentOS:" &&
python --version &&
echo "pip version in this CentOS:" &&
pip --version &&
exit 0
