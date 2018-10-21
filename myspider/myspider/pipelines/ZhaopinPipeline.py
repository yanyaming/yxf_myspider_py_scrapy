# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem

#requirments
import pymongo

from myspider.settings import NOSQL_DB


class  MongodbdbPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb://{}:{}/".format(NOSQL_DB['HOST'],NOSQL_DB['PORT']))#连接数据库
        self.mongodb = self.conn[NOSQL_DB['DBNAME']]#选择数据库
        self.mongodb_table = self.mongodb[NOSQL_DB['COLLECTION']]#选择表

    #执行操作：判断数据是否已存在，若不存在则存入数据库，若存在则丢掉
    def process_item(self, item, spider):
        if not self.is_item_exist(item):
            self.mongodb_table.insert(dict(item))
            # logging.debug("Question added to MongoDB NOSQL_DB!")
        else:
            raise DropItem("{} is exist".format(item['url']))
        return item

    #判断是否已存在此数据，若存在则返回True
    def is_item_exist(self, item):
        if self.mongodb_table.find_one({"url": item['url']}):
            return True
        else:
            return False
