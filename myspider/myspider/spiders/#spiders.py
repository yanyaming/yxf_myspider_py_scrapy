# -*- coding: utf-8 -*-
import scrapy


'''
extract()——返回最终结果，不再嵌套解析
extract_first()——返回第一条
'''


class MySpider(scrapy.Spider):

    # 爬虫程序名称，scrapy crawl myspider
    name = 'myspider'

    # 允许爬取的域名
    allowed_domains = ['domain.com']

    # 针对特定爬虫的自定义设置
    custom_settings = {
        'ITEM_PIPELINES': {
            'myspider.pipelines.UrlPipeline': 100,
            'myspider.pipelines.pipelines': 200,
        }
    }

    # 初始URL，添加到任务队列
    start_urls = [
        'https://domain.com/page1',
        'https://domain.com/page2',
    ]

    @classmethod
    def from_crawler(cls, crawler):
        # scrapy风格的实例化入口，功能类似__init__，在__init__之前执行，会自动生成crowler和settings属性
        return cls()

    def start_requests(self):
        # 爬虫启动时自动发出的首个请求（覆盖start_urls），只执行一次。最典型场景就是登录
        return [scrapy.FormRequest("http://www.example.com/login",
            formdata={'user': 'john', 'pass': 'secret'},
            callback=self._logged_in)]

    def parse(self, response):
        # 如果Request未指定callback则自动调用此方法，执行对响应网页的解析，解析得到项目
        # yield把item传递给pipeline处理
        for i in result:
            yield i

    def closed(self, reason):
        # 爬虫关闭时的操作
        pass

    def _logged_in(self, response):
        # 自定义方法
        # 解析登录后的网页并发出新请求
        return response
