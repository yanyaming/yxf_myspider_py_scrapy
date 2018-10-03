#!/bin/sh
#install shadowsocks
pip install shadowsocks &&
#install config file
mkdir -p /etc/shadowsocks && cp -f ./shadowsocks.json /etc/shadowsocks/shadowsocks.json &&
#set as a server
sudo cp -f ./shadowsocks.service /usr/lib/systemd/system/shadowsocks.service &&
sudo chmod 754 /usr/lib/systemd/system/shadowsocks.service &&
sudo systemctl enable shadowsocks &&
#firewall
firewall-cmd --zone=public --add-port=50003/tcp --permanent &&
firewall-cmd --reload &&
echo "check service:"
systemctl status shadowsocks &&
exit 0
