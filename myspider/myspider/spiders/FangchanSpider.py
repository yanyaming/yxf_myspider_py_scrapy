#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from scrapy_redis.spiders import RedisSpider
import scrapy
from myspider.pipelines.FangchanItem import AnjukeZufangItem


#继承自RedisSpider，则start_urls可以从redis读取
#测试所有代理，几乎全是302重定向到验证码页面
class AnjukeZufangSpider(RedisSpider):
    success=0
    name = 'fangchan_anjuke_zufang'
    allowed_domains = ['anjuke.ccom']
    custom_settings = {
        'ITEM_PIPELINES': {
            'myspider.pipelines.FangchanPipeline.AnjukeZufangPipeline': 300,
        },
        'PROXY': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATICWITHPROXY':True,
    }

    def parse(self, response):
        if response.status==200:
            self.success+=1
            print("success num:"+str(self.success))
        yield scrapy.Request(url=response.request.url,headers=response.request.headers, meta=response.request.meta).replace(dont_filter=True)

        # list_content = response.css('.list-content .zu-itemmod')
        # for i in list_content:
        #     item = AnjukeZufangItem()
        #     #编码
        #     bianma = i.css('.zu-itemmod .zu-info h3 a::attr(href)').extract_first().split('/')[-1]
        #     #标题
        #     item.biaoti = str(i.css('.zu-itemmod .zu-info h3 a::attr(title)').extract_first())
        #     #图片（文件）
        #     item.tupian = str(i.css('.zu-itemmod .thumbnail::attr(src)').extract_first())
        #     #费用
        #     item.feiyong = str(i.css('.zu-itemmod .zu-side strong::text').extract_first())+str(i.css('.zu-side p::text').extract())
        #     #地址
        #     item.dizhi = str(response.css('.zu-itemmod .zu-info address::text').extract_first())
        #     #小区
        #     item.xiaoqu = str(response.css('.zu-itemmod .zu-info address a::text').extract_first())
        #     #户型
        #     item.huxing = str(response.css('.zu-itemmod .zu-info').xpath('//*p[1]/text()[1]').extract_first())
        #     #面积
        #     item.mianji = str(response.css('.zu-itemmod .zu-info').xpath('//*p[1]/text()[2]').extract_first())
        #     #楼层
        #     item.louceng = str(response.css('.zu-itemmod .zu-info').xpath('//*p[1]/text()[3]').extract_first())
        #     #联系人
        #     item.lianxiren = str(response.css('.zu-itemmod .zu-info').xpath('//*p[1]/text()[4]').extract_first())
        #     #租赁方式
        #     item.zulinfangshi = str(response.css('.zu-itemmod .zu-info').xpath('//*p[2]/span[1]/text()').extract_first())
        #     #朝向
        #     item.chaoxiang = str(response.css('.zu-itemmod .zu-info').xpath('//*p[2]/span[2]/text()').extract_first())
        #     #附近地铁
        #     item.fujinditie = str(response.css('.zu-itemmod .zu-info').xpath('//*p[2]/span[3]/text()').extract_first())
        #     #url:详情页
        #     url_detailpage=response.css('.zu-itemmod div::attr(link)').extract_first()
        #     print('----------------------'+str(item))
        #     yield scrapy.Request(url=url_detailpage,callback=self.parsedetail)
        #     yield item
        # #url:下一页
        # url_nextpage=response.css('.aNxt::attr(href)').extract_first()
        # yield scrapy.Request(url=url_nextpage)

    # callback可在一个爬虫里递进深入爬取
    def parsedetail(self, response):
        item = AnjukeZufangItem()
        #编码
        bianma = str(response.url.split('/')[-1])
        #装修程度
        item.zhuangxiuchengdu = response.css('.house-info-zufang').xpath('//*li[6]/span[2]/text()').extract_first()
        #住宅类型
        item.zhuzhaileixing = response.css('.house-info-zufang').xpath('//*li[7]/span[2]/text()').extract_first()
        #户型明细
        item.huxingmingxi = response.css('.house-info-zufang').xpath('//*li[2]/span[2]/text()').extract_first()
        #付款类型
        item.fukuanleixing = response.css('.house-info-zufang').xpath('//*li[1]/span[2]/text()').extract_first()
        #发布时间
        item.fabushijian = response.css('.right-info::text').extract_first().split('发布时间：')[1]
        #房屋配套（列表）
        item.fangwupeitao = response.css('.house-info-peitao .has div::text').extract()
        #房源概况（长文本）
        item.fangyuangaikuang = response.css('.auto-general::text').extract_first()
        #小区问答（长文本）
        item.xiaoquwenda = response.css('.comm-qa').xpath('//*text()').extract_first()
        print('----------------------'+str(item))
        yield item

#测试免费代理可行
class FangtianxiaZufangSpider(RedisSpider):
    success = 0
    name = 'fangchan_fangtianxia_zufang'
    allowed_domains = ['fang.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            # 'myspider.pipelines.FangchanPipeline.AnjukeZufangPipeline': 300
        },
        'PROXY': True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATICWITHPROXY':True,
    }

    def parse(self, response):
        if response.status==200:
            self.success+=1
            print("success num:"+str(self.success))
        yield scrapy.Request(url=response.request.url,headers=response.request.headers, meta=response.request.meta).replace(dont_filter=True)


#测试免费代理可行
class WubatongchengZufangSpider(RedisSpider):
    success=0
    name = 'fangchan_58_zufang'
    allowed_domains = ['58.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            # 'myspider.pipelines.FangchanPipeline.AnjukeZufangPipeline': 300
        },
        'PROXY':True,
        'PROXY_MAX_USE': 10,
        'PROXY_FROM_WHERE': 'server',
        'HEADER_STATICWITHPROXY': True,
    }

    def parse(self, response):
        if response.status==200:
            self.success+=1
            print("success num:"+str(self.success))
        yield scrapy.Request(url=response.request.url,headers=response.request.headers, meta=response.request.meta).replace(dont_filter=True)
