# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import redis  #数据库操作库
import pymongo
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
from .settings_cfg.py import Database, Queue_Db, IP_Proxy_API, IP_Proxy_Page, Master_Server

class UrlQueuePipeline(object):
    def __init__(self):
        self.redis_table = Queue_db['DBNAME']  # 选择表
        self.redis_db = redis.Redis(host=Queue_db['HOST'], port=Queue_db['PORT'], db=Queue_db['DB'])  # redis数据库连接信息

    def process_item(self, item, spider):
        if self.redis_db.exists(item['url']):
            raise DropItem('%s id exists!!' % (item['url']))
        else:
            self.redis_db.lpush(self.redis_table, item['url'])
        return item

class  MgdbPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://{}:{}/".format(Database['HOST'],Database['PORT']))
        self.db = self.conn[Database['DBNAME']] #选择数据库
        self.MG_table = self.db[Database['COLLECTION']] #选择表

    def process_item(self, item, spider):
        if not self.is_item_exist(item):
            self.MG_table.insert(dict(item))
            logging.debug("Question added to MongoDB database!")
            # log.msg("Question added to MongoDB database!", level=log.DEBUG, spider=spider)
            '''
            Scrapy 提供 5 层 logging 级别：
            CRITICAL - 严重错误(critical)
            ERROR - 一般错误(regular errors)
            WARNING - 警告信息(warning messages)
            INFO - 一般信息(informational messages)
            DEBUG - 调试信息(debugging messages)     本程序用的就是DEBUG

            '''
        else:
            raise DropItem("{} is exist".format(item['url']))
        return item

    def is_item_exist(self, item):
        if self.MG_table.find_one({"url": item['url']}):
            return True
        else:
            return False
