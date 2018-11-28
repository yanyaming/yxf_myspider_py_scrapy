#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
from scrapy.loader.processors import MapCompose,TakeFirst  #添加继续处理函数,选取第一个元素
from scrapy.loader import ItemLoader  #预定义网页选取规则
import psycopg2
import psycopg2.pool
from myspider.settings import DATABASE,DATABASE_URL


class DefaultItemLoader(ItemLoader):
    default_output_processor=TakeFirst()

    def __init__(self,item,response):
        super(DefaultItemLoader,self).__init__(item=item,response=response)

# def postgresConn(pool_max=1,pool_min=1):
#     return #conn obj


class SavePipeline(object):
    def __init__(self):
        # self.db = psycopg2.connect()
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_item(self, item, spider):
        # self.db[spider.name].update(item.bianma,dict(item),upsert=True)
        raise DropItem("save to db ok: %s" % item)
