#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from myspider.settings import BASE_DIR
from selenium import common
from selenium import webdriver
from selenium.webdriver.common.proxy import *

'''
用于css/js渲染、访问附带文件、执行浏览器操作。
这里的selenium为版本3，包含common和webdriver两个子包，common只有异常处理代码，webdriver是主体。
其中webdriver包含各种浏览器的驱动代码以及common公共代码。
chromedriver还要额外安装chrome浏览器，麻烦，不用。
'''


def load_firefox(load_images=True, display=True, proxy=''):
    firefox_profile = webdriver.FirefoxProfile()
    firefox_options = webdriver.FirefoxOptions()
    if not display:  # 不显示界面
        firefox_options.set_headless()
    else:
        pass
    if not load_images:  # 不加载图片
        firefox_profile.set_preference('browser.migration.version', 9001)
        firefox_profile.set_preference('permissions.default.image', 2)
    else:
        pass
    if proxy:
        proxy_ip = proxy.split('://')[1].split(':')[0]
        proxy_port = int(proxy.split('://')[1].split(':')[1])
        firefox_profile.set_preference("network.proxy.type", 1)  # 是否启用代理,1启用
        firefox_profile.set_preference("network.proxy.http", proxy_ip)
        firefox_profile.set_preference("network.proxy.http_port", proxy_port)
        firefox_profile.set_preference("network.proxy.share_proxy_settings", False)  # 是否全局共享,False不共享
        firefox_profile.set_preference("network.proxy.no_proxies_on", "localhost")  # 例外
    else:
        pass
    browser = webdriver.Firefox(
        executable_path=os.path.join(BASE_DIR, 'webdriver/geckodriver'),
        firefox_profile=firefox_profile,
        firefox_options=firefox_options,
        timeout=10,
    )
    return browser


def load_chrome(load_images=True, display=True):
    chrome_options = webdriver.ChromeOptions()
    if not display:  # 不显示界面
        chrome_options.set_headless()
    else:
        pass
    if not load_images:  # 不加载图片
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
    else:
        pass
    browser = webdriver.Chrome(
        executable_path=os.path.join(BASE_DIR, 'webdriver/chromedriver'),
        chrome_options=chrome_options,
    )
    return browser


def load_phantomjs():
    browser = webdriver.PhantomJS(
        executable_path=os.path.join(BASE_DIR, 'webdriver/phantomjs'),
    )
    return browser
