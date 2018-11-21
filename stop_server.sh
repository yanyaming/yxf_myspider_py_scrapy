#!/bin/sh
kill -9 $(netstat -npl | grep :8001 | awk '{print $7}' | awk -F"/" '{ print $1 }')
kill -9 $(netstat -npl | grep :6800 | awk '{print $7}' | awk -F"/" '{ print $1 }')
kill -9 $(netstat -npl | grep :8080 | awk '{print $7}' | awk -F"/" '{ print $1 }')
echo "server is stoped."
exit 0
