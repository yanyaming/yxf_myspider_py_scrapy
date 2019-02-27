#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import sys
import os
import requests
import json
import time
from myspider.downloaders import myselenium
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    # browser = myselenium.load_firefox(load_images=False,display=False)
    # browser.get('https://blog.csdn.net/lbxoqy/article/details/70052375')
    # browser.get_screenshot_as_file('screensoot.png')
    # # time.sleep(10)
    # browser.close()
    # # time.sleep(10)
    # # browser.quit()
    test_url = 'http://httpbin.org/get'
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }
    proxies = {"http": "http://134.119.205.248:8080",}
    r = requests.get(url=test_url, headers=headers, timeout=5, proxies=proxies)
    if r.ok:
        content = json.loads(r.text)
        print(content)
        headers = content['headers']
        ip = content['origin']
        proxy_connection = headers.get('Proxy-Connection', None)
        if ',' in ip:
            ip1 = ip.split(', ')[0]
            ip2 = ip.split(', ')[1]
            if ip1 == ip2:
                types = 0
            else:
                types = 2
        elif proxy_connection:
            types = 1
        else:
            types = 0
        print(types)
