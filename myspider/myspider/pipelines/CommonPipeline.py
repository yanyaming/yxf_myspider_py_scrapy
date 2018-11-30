#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from sqlalchemy import Column, create_engine
from sqlalchemy import String, Integer  # 数据字段类型
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from myspider.settings import DATABASE,DATABASE_URL


Base = declarative_base()
# 初始化数据库连接:
engine = create_engine(DATABASE_URL)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


class SavePipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        self.session.add(item)
        self.session.commit()

    def close_spider(self, spider):
        self.session.close()
