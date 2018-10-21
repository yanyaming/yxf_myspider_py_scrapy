# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem

#requirments
import redis

from myspider.settings import QUEUE_DB


class RedisPipeline(object):
    def __init__(self):
        self.redis = redis.Redis(host=QUEUE_DB['HOST'], port=QUEUE_DB['PORT'], db=QUEUE_DB['DB'])#连接数据库
        self.redis_table = QUEUE_DB['DBNAME']#选择表

    #执行操作：判断url是否已存在，若不存在则存入队列，若存在则丢掉
    def process_item(self, item, spider):
        if self.redis.exists(item['url']):
            raise DropItem('%s id exists!!' % (item['url']))
        else:
            self.redis.lpush(self.redis_table, item['url'])
        return item
