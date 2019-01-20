#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from myspider.settings import BASE_DIR
from selenium import common
from selenium import webdriver
from pyvirtualdisplay import Display

'''
这里的selenium为版本3，包含common和webdriver两个子包，common只有异常处理代码，webdriver是主体。
其中webdriver包含各种浏览器的驱动代码以及common公共代码。
'''


class Firefox:
    def __init__(self):
        self.browser = None

    def load(self):
        self.browser = webdriver.Firefox(executable_path=os.path.join(BASE_DIR, 'webdriver/chromedriver'))


class Chrome:
    def __init__(self):
        self.browser = None

    def load(self, load_images=True, display=True):
        if not display:
            display = Display(visible=0, size=(800, 600))
            display.start()
        else:
            pass
        if not load_images:  # 不加载图片
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.managed_default_content_settings.images": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            self.browser = webdriver.Chrome(
                executable_path=os.path.join(BASE_DIR, 'webdriver/chromedriver'),
                chrome_options=chrome_options
            )
        else:
            self.browser = webdriver.Chrome(
                executable_path=os.path.join(BASE_DIR, 'webdriver/chromedriver')
            )
        return self.browser


class Phantomjs:
    def __init__(self):
        self.browser = None

    def load(self):
        self.browser = webdriver.PhantomJS(executable_path=os.path.join(BASE_DIR, 'webdriver/chromedriver'))

