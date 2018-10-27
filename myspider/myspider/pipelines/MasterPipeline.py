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


class RedisPipeline(object):
    def __init__(self):
        self.redis = redis.Redis(crawler.setting.get('REDIS_URI'))#连接数据库

    #执行操作：首先判断item是否为url，判断url是否已存在，若不存在则存入队列，若存在则丢掉
    def process_item(self, item, spider):
        if not url:
            return item
        else:
            if self.redis.exists(item['url']):
                raise DropItem('%s id exists!!' % (item['url']))
            else:
                self.redis.lpush(self.redis_table, item['url'])
            return item
