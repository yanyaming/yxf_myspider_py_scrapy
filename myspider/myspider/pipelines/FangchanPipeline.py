#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class  AnjukeZufangPipeline(object):
    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_item(self, item, spider):
        #process
        #数据去重，数据规范化
        return item
