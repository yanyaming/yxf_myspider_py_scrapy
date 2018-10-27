# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class  MyspiderPipeline(object):
    def __init__(self):
        #__init__
        self.ids_seen = set()

    @classmethod
    def from_crawler(cls, crawler):
        # scrapy风格的实例化入口，功能类似__init__，在__init__之前执行，会自动生成crowler和settings属性
        return cls()

    def open_spider(self, spider):
        # 爬虫启动时的动作
        self.file = open('items.json', 'w')

    def close_spider(self, spider):
        # 爬虫关闭时的动作
        self.file.close()

    def process_item(self, item, spider):
        # 处理项目
        #
        # 返回值可选:
        # item:继续传递给其他pipeline
        # 不返回，raise DropItem:丢掉此项目，不再处理
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
