#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy


class MyspiderItem(scrapy.Item):
    name = scrapy.Field()
