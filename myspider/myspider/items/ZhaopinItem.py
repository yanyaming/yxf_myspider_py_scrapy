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
    # 要求
    yaoqiu = scrapy.Field()
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

    # info
    crawl_time = scrapy.Field()

    def parse_detailpage_qianchengwuyou(self, response):
        self['_id'] = str(response.url.split('?')[0].split('/')[-1].split('.')[0])
        self['pingtai'] = '前程无忧 51job'
        self['chengshi'] = response.css('.tHeader .msg::attr(title)').extract_first().split('|')[0].strip().split('-')[0]
        self['yaoqiu'] = response.css('.tHeader .msg::attr(title)').extract_first().split('|')
        for i,ite in enumerate(self['yaoqiu']):
            self['yaoqiu'][i] = ite.strip()
        self['shangbandizhi'] = response.css('.tCompany_main').xpath('./div[@class="tBorderTop_box"][2]/div/p/text()[2]').extract_first()
        self['zhiweimingcheng'] = response.css('.tHeader .cn h1::attr(title)').extract_first()
        self['zhiweibiaoqian'] = response.css('.tHeader .jtag .sp4::text').extract()
        self['zhiweixinxi'] = str(response.css('.tCompany_main').xpath('./div[@class="tBorderTop_box"][1]/div/p').extract())
        self['zhiweigongzi'] = response.css('.tHeader .cn strong::text').extract_first()
        self['gongsimingcheng'] = response.css('.tHeader .cname a::attr(title)').extract_first()
        self['gongsileixing'] = response.css('.tCompany_sidebar .com_tag').xpath('./p[1]/@title').extract_first()
        self['gongsirenshu'] = response.css('.tCompany_sidebar .com_tag').xpath('./p[2]/@title').extract_first()
        self['gongsihangye'] = response.css('.tCompany_sidebar .com_tag').xpath('./p[3]/@title').extract_first()
        self['gongsixinxi'] = response.css('.tCompany_main').xpath('./div[@class="tBorderTop_box"][3]/div/text()').extract_first()
