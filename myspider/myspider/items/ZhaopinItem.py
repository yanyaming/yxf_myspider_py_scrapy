# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#item定义每一条数据的所有字段映射到数据库，字段数据类型自动根据实际数据确定

class MyspiderItem(scrapy.Item):
    name = scrapy.Field()
