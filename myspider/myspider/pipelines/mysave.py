#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymongo
from scrapy.exceptions import DropItem
from myspider.settings import DATABASE,DATABASE_URL


class MySavePipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(DATABASE_URL)

    def process_item(self, item, spider):
        data = dict(item)
        # spider.logger.info('MySavePipeline----------item:' + str(data))
        db = self.client[DATABASE['db']]
        co = db[spider.name]
        co.save(data)
        raise DropItem
