#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy

#除了图片，其他一律存储为字符串
class AnjukeZufangItem(scrapy.Item):

    #listpage
    #编码
    bianma = scrapy.Field()
    #标题
    biaoti = scrapy.Field()
    #图片（图片）
    tupian = scrapy.Field()
    #费用
    feiyong = scrapy.Field()
    #地址
    dizhi = scrapy.Field()
    #小区
    xiaoqu = scrapy.Field()
    #户型
    huxing = scrapy.Field()
    #楼层
    louceng = scrapy.Field()
    #面积
    mianji = scrapy.Field()
    #租赁方式
    zulinfangshi = scrapy.Field()
    #联系人
    lianxiren = scrapy.Field()
    #朝向
    chaoxiang = scrapy.Field()
    #附近地铁
    fujinditie = scrapy.Field()

    #detailpage
    #装修程度
    zhuangxiuchengdu = scrapy.Field()
    #住宅类型
    zhuzhaileixing = scrapy.Field()
    #户型明细
    huxingmingxi = scrapy.Field()
    #付款类型
    fukuanleixing = scrapy.Field()
    #发布时间
    fabushijian = scrapy.Field()
    #房屋配套（列表）
    fangwupeitao = scrapy.Field()
    #房源概况（长文本）
    fangyuangaikuang = scrapy.Field()
    #小区问答（长文本）
    xiaoquwenda = scrapy.Field()

class AnjukeXinfangItem(scrapy.Item):
    pass

class AnjukeErshoufangItem(scrapy.Item):
    pass
