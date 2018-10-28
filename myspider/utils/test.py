#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymongo

conn = pymongo.MongoClient("mongodb://{}:{}@{}:{}/myspider".format('myspideruser','Yanyaming250114sv1','173.82.95.81','27017'))#连接数据库
db = conn['myspider']#选择数据库
collection = db['test']#选择表
print(collection)