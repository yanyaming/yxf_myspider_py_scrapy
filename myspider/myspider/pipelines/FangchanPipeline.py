#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import traceback
from scrapy.exceptions import DropItem

#requirments
import pymongo


class  AnjukeZufangPipeline(object):
    def __init__(self):
        try:
            self.db = pymongo.MongoClient(self.MONGODB_URI)
        except Exception as e:
            traceback.print_exc()

    @classmethod
    def from_crawler(cls, crawler):
        cls.MONGODB_URI = crawler.settings.get('MONGODB_URI')
        pipe = cls()
        pipe.crawler = crawler
        return pipe

    def process_item(self, item, spider):
        self.db[spider.name].update(item.bianma,dict(item),upsert=True)
        logging.debug("added to MongoDB")
        return item
