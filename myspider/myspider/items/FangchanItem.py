#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy

'''
1.Field()建立scrapy数据对象字段，在spider里yield item就可以被pipeline截获
2.在class中记录静态解析规则
'''


#1
class fangchan_anjuke_zufang_item(scrapy.Item):
    # listpage
    # id
    _id = scrapy.Field()
    # 城市
    chengshi = scrapy.Field()
    # 标题
    biaoti = scrapy.Field()
    # 图片（文件）
    tupian = scrapy.Field()
    # 费用
    feiyong = scrapy.Field()
    # 地址
    dizhi = scrapy.Field()
    # 小区
    xiaoqu = scrapy.Field()
    # 户型
    huxing = scrapy.Field()
    # 楼层
    louceng = scrapy.Field()
    # 面积
    mianji = scrapy.Field()
    # 租赁方式
    zulinfangshi = scrapy.Field()
    # 联系人
    lianxiren = scrapy.Field()
    # 朝向
    chaoxiang = scrapy.Field()
    # 附近地铁
    fujinditie = scrapy.Field()

    # detailpage
    # 装修程度
    zhuangxiuchengdu = scrapy.Field()
    # 住宅类型
    zhuzhaileixing = scrapy.Field()
    # 户型明细
    huxingmingxi = scrapy.Field()
    # 付款类型
    fukuanleixing = scrapy.Field()
    # 发布时间
    fabushijian = scrapy.Field()
    # 房屋配套（列表）
    fangwupeitao = scrapy.Field()
    # 房源概况（长文本）
    fangyuangaikuang = scrapy.Field()
    # 小区问答（长文本）
    xiaoquwenda = scrapy.Field()

    # info
    crawl_time = scrapy.Field()

    def parse_listpage(self, response, ite):
        #id
        self['_id'] = ite.css('.zu-itemmod .zu-info h3 a::attr(href)').extract_first().split('/')[-1]
        #城市
        self['chengshi'] = str(response.css('.breadcrumbs div a::text').extract_first())[:-3]
        #标题
        self['biaoti'] = ite.css('.zu-itemmod .zu-info h3 a::attr(title)').extract_first()
        #图片（链接）
        self['tupian'] = ite.css('.zu-itemmod .thumbnail::attr(src)').extract_first()
        #费用
        self['feiyong'] = str(ite.css('.zu-itemmod .zu-side strong::text').extract_first())+str(ite.css('.zu-side p::text').extract_first())
        #地址
        self['dizhi'] = response.css('.zu-itemmod .zu-info').xpath('./address/text()[2]').extract_first().strip()
        #小区
        self['xiaoqu'] = response.css('.zu-itemmod .zu-info address a::text').extract_first()
        #户型
        self['huxing'] = response.css('.zu-itemmod .zu-info').xpath('./p[1]/text()[1]').extract_first().strip()
        #面积
        self['mianji'] = response.css('.zu-itemmod .zu-info').xpath('./p[1]/text()[2]').extract_first()
        #楼层
        self['louceng'] = response.css('.zu-itemmod .zu-info').xpath('./p[1]/text()[3]').extract_first()
        #联系人
        self['lianxiren'] = response.css('.zu-itemmod .zu-info').xpath('./p[1]/text()[4]').extract_first().strip()
        #租赁方式
        self['zulinfangshi'] = response.css('.zu-itemmod .zu-info').xpath('./p[2]/span[1]/text()').extract_first()
        #朝向
        self['chaoxiang'] = response.css('.zu-itemmod .zu-info').xpath('./p[2]/span[2]/text()').extract_first()
        #附近地铁
        self['fujinditie'] = response.css('.zu-itemmod .zu-info').xpath('./p[2]/span[3]/text()').extract_first()

    def parse_detailpage(self, response):
        #装修程度
        self['zhuangxiuchengdu'] = response.css('.house-info-zufang').xpath('./li[6]/span[2]/text()').extract_first()
        #住宅类型
        self['zhuzhaileixing'] = response.css('.house-info-zufang').xpath('./li[7]/span[2]/text()').extract_first()
        #户型明细
        self['huxingmingxi'] = response.css('.house-info-zufang').xpath('./li[2]/span[2]/text()').extract_first()
        #付款类型
        self['fukuanleixing'] = response.css('.house-info-zufang').xpath('./li[1]/span[2]/text()').extract_first()
        #发布时间
        self['fabushijian'] = response.css('.right-info::text').extract_first().split('发布时间：')[1]
        #房屋配套（列表）
        self['fangwupeitao'] = response.css('.house-info-peitao .has div::text').extract()
        #房源概况（长文本）
        self['fangyuangaikuang'] = response.css('.auto-general::text').extract_first().strip()


#2
class fangchan_anjuke_xinfang_item(scrapy.Item):
    pass


#3
class fangchan_anjuke_ershoufang_item(scrapy.Item):
    pass


#4
class fangchan_fangtianxia_zufang_item(scrapy.Item):
    pass


#5
class fangchan_fangtianxia_xinfang_item(scrapy.Item):
    pass


#6
class fangchan_fangtianxia_ershoufang_item(scrapy.Item):
    pass


#7
class fangchan_wubatongcheng_zufang_item(scrapy.Item):
    pass
