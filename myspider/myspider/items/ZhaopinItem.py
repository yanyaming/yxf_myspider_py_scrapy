#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scrapy


class zhaopin_item(scrapy.Item):
    #id
    _id = scrapy.Field()
    # 平台
    pingtai = scrapy.Field()
    # 城市
    chengshi = scrapy.Field()
    # 地区
    diqu = scrapy.Field()
    # 经验要求
    jingyanyaoqiu = scrapy.Field()
    # 学历要求
    xueliyaoqiu = scrapy.Field()
    # 招聘人数
    zhaopinrenshu = scrapy.Field()
    # 发布日期
    faburiqi = scrapy.Field()
    # 上班地址
    shangbandizhi = scrapy.Field()
    # 职位名称
    zhiweimingcheng = scrapy.Field()
    # 职位标签
    zhiweibiaoqian = scrapy.Field()
    # 职位信息（长文本）
    zhiweixinxi = scrapy.Field()
    # 职位工资
    zhiweigongzi = scrapy.Field()
    # 公司名称
    gongsimingcheng = scrapy.Field()
    # 公司类型
    gongsileixing = scrapy.Field()
    # 公司人数
    gongsirenshu = scrapy.Field()
    # 公司行业
    gongsihangye = scrapy.Field()
    # 公司信息（长文本）
    gongsixinxi = scrapy.Field()

    def parse_detailpage_qianchengwuyou(self, response):
        self['zhuangxiuchengdu'] = response.css('.house-info-zufang').xpath('./li[6]/span[2]/text()').extract_first()
