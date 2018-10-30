#!/bin/sh
firewall-cmd --zone=public --add-port=8001/tcp --permanent &&
firewall-cmd --zone=public --add-port=6800/tcp --permanent &&
firewall-cmd --reload &&
exit 0
