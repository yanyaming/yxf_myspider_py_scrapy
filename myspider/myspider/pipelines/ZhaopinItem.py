# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    name = scrapy.Field()
