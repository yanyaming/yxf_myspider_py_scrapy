#!/bin/sh
kill -9 $(netstat -npl | grep :8001 | awk '{print $7}' | awk -F"/" '{ print $1 }')
kill -9 $(netstat -npl | grep :6800 | awk '{print $7}' | awk -F"/" '{ print $1 }')
kill -9 $(netstat -npl | grep :8080 | awk '{print $7}' | awk -F"/" '{ print $1 }')
kill -9 $(netstat -npl | grep :5000 | awk '{print $7}' | awk -F"/" '{ print $1 }')
#docker stop $(docker ps -a -q)
echo "server is stoped."
exit 0
