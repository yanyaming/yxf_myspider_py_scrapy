#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy
from sqlalchemy import Column, create_engine
from sqlalchemy import String, Integer  # 数据字段类型
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from myspider.settings import DATABASE_URL, DATABASE

'''
1.scrapy框架的Item类与sqlalchemy的Base类组合编程:
    Column()建立sqlalchemy数据对象字段
    Field()建立scrapy数据对象字段
2.在class中记录静态解析规则
'''

Base = declarative_base()
# 初始化数据库连接:
engine = create_engine(DATABASE_URL)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# class AnjukeZufangItem(scrapy.Item):
#     #listpage
#     #编码
#     bianma = scrapy.Field()
#     #标题
#     biaoti = scrapy.Field()
#     #图片（文件）
#     tupian = scrapy.Field()
#     #费用
#     feiyong = scrapy.Field()
#     #地址
#     dizhi = scrapy.Field()
#     #小区
#     xiaoqu = scrapy.Field()
#     #户型
#     huxing = scrapy.Field()
#     #楼层
#     louceng = scrapy.Field()
#     #面积
#     mianji = scrapy.Field()
#     #租赁方式
#     zulinfangshi = scrapy.Field()
#     #联系人
#     lianxiren = scrapy.Field()
#     #朝向
#     chaoxiang = scrapy.Field()
#     #附近地铁
#     fujinditie = scrapy.Field()
# 
#     #detailpage
#     #装修程度
#     zhuangxiuchengdu = scrapy.Field()
#     #住宅类型
#     zhuzhaileixing = scrapy.Field()
#     #户型明细
#     huxingmingxi = scrapy.Field()
#     #付款类型
#     fukuanleixing = scrapy.Field()
#     #发布时间
#     fabushijian = scrapy.Field()
#     #房屋配套（列表）
#     fangwupeitao = scrapy.Field()
#     #房源概况（长文本）
#     fangyuangaikuang = scrapy.Field()
#     #小区问答（长文本）
#     xiaoquwenda = scrapy.Field()
# 
#     #info
#     crawl_time = scrapy.Field()
#     crawl_update_time = scrapy.Field()
    

class fangchan_anjuke_zufang_item(Base, scrapy.Item):
    __tablename__ = "fangchan_anjuke_zufang"
    id = Column(Integer, primary_key=True, autoincrement=True)

    # listpage
    # 编码
    bianma = Column(String)
    # 标题
    biaoti = Column(String)
    # 图片（文件）
    tupian = Column(String)
    # 费用
    feiyong = Column(String)
    # 地址
    dizhi = Column(String)
    # 小区
    xiaoqu = Column(String)
    # 户型
    huxing = Column(String)
    # 楼层
    louceng = Column(String)
    # 面积
    mianji = Column(String)
    # 租赁方式
    zulinfangshi = Column(String)
    # 联系人
    lianxiren = Column(String)
    # 朝向
    chaoxiang = Column(String)
    # 附近地铁
    fujinditie = Column(String)

    # detailpage
    # 装修程度
    zhuangxiuchengdu = Column(String)
    # 住宅类型
    zhuzhaileixing = Column(String)
    # 户型明细
    huxingmingxi = Column(String)
    # 付款类型
    fukuanleixing = Column(String)
    # 发布时间
    fabushijian = Column(String)
    # 房屋配套（列表）
    fangwupeitao = Column(String)
    # 房源概况（长文本）
    fangyuangaikuang = Column(String)
    # 小区问答（长文本）
    xiaoquwenda = Column(String)

    # info
    crawl_time = Column(String)
    crawl_update_time = Column(String)

    def parse_listpage(self, response, i):
        #编码
        self.bianma = i.css('.zu-itemmod .zu-info h3 a::attr(href)').extract_first().split('/')[-1]
        #标题
        self.biaoti = str(i.css('.zu-itemmod .zu-info h3 a::attr(title)').extract_first())
        #图片（文件）
        self.tupian = str(i.css('.zu-itemmod .thumbnail::attr(src)').extract_first())
        #费用
        self.feiyong = str(i.css('.zu-itemmod .zu-side strong::text').extract_first())+str(i.css('.zu-side p::text').extract())
        #地址
        self.dizhi = str(response.css('.zu-itemmod .zu-info address::text').extract_first())
        #小区
        self.xiaoqu = str(response.css('.zu-itemmod .zu-info address a::text').extract_first())
        #户型
        self.huxing = str(response.css('.zu-itemmod .zu-info').xpath('//*p[1]/text()[1]').extract_first())
        #面积
        self.mianji = str(response.css('.zu-itemmod .zu-info').xpath('//*p[1]/text()[2]').extract_first())
        #楼层
        self.louceng = str(response.css('.zu-itemmod .zu-info').xpath('//*p[1]/text()[3]').extract_first())
        #联系人
        self.lianxiren = str(response.css('.zu-itemmod .zu-info').xpath('//*p[1]/text()[4]').extract_first())
        #租赁方式
        self.zulinfangshi = str(response.css('.zu-itemmod .zu-info').xpath('//*p[2]/span[1]/text()').extract_first())
        #朝向
        self.chaoxiang = str(response.css('.zu-itemmod .zu-info').xpath('//*p[2]/span[2]/text()').extract_first())
        #附近地铁
        self.fujinditie = str(response.css('.zu-itemmod .zu-info').xpath('//*p[2]/span[3]/text()').extract_first())

    def parse_detailpage(self, response, i=None):
        #编码
        self.bianma = str(response.url.split('/')[-1])
        #装修程度
        self.zhuangxiuchengdu = response.css('.house-info-zufang').xpath('//*li[6]/span[2]/text()').extract_first()
        #住宅类型
        self.zhuzhaileixing = response.css('.house-info-zufang').xpath('//*li[7]/span[2]/text()').extract_first()
        #户型明细
        self.huxingmingxi = response.css('.house-info-zufang').xpath('//*li[2]/span[2]/text()').extract_first()
        #付款类型
        self.fukuanleixing = response.css('.house-info-zufang').xpath('//*li[1]/span[2]/text()').extract_first()
        #发布时间
        self.fabushijian = response.css('.right-info::text').extract_first().split('发布时间：')[1]
        #房屋配套（列表）
        self.fangwupeitao = response.css('.house-info-peitao .has div::text').extract()
        #房源概况（长文本）
        self.fangyuangaikuang = response.css('.auto-general::text').extract_first()
        #小区问答（长文本）
        self.xiaoquwenda = response.css('.comm-qa').xpath('//*text()').extract_first()


class fangchan_anjuke_xinfang_item(scrapy.Item):
    pass


class fangchan_anjuke_ershoufang_item(scrapy.Item):
    pass


class fangchan_fangtianxia_zufang_item(scrapy.Item):
    pass


class fangchan_fangtianxia_xinfang_item(scrapy.Item):
    pass


class fangchan_fangtianxia_ershoufang_item(scrapy.Item):
    pass


class fangchan_wubatongcheng_zufang_item(scrapy.Item):
    pass
