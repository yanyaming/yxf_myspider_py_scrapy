#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from myspider.settings import BASE_DIR
from selenium import common
from selenium import webdriver

'''
这里的selenium为版本3，包含common和webdriver两个子包，common只有异常处理代码，webdriver是主体。
其中webdriver包含各种浏览器的驱动代码以及common公共代码。

selenium/webdriver/__init__.py:
from .firefox.webdriver import WebDriver as Firefox  # noqa
from .firefox.firefox_profile import FirefoxProfile  # noqa
from .firefox.options import Options as FirefoxOptions  # noqa
from .chrome.webdriver import WebDriver as Chrome  # noqa
from .chrome.options import Options as ChromeOptions  # noqa
from .ie.webdriver import WebDriver as Ie  # noqa
from .ie.options import Options as IeOptions  # noqa
from .edge.webdriver import WebDriver as Edge  # noqa
from .opera.webdriver import WebDriver as Opera  # noqa
from .safari.webdriver import WebDriver as Safari  # noqa
from .blackberry.webdriver import WebDriver as BlackBerry  # noqa
from .phantomjs.webdriver import WebDriver as PhantomJS  # noqa
from .android.webdriver import WebDriver as Android  # noqa
from .webkitgtk.webdriver import WebDriver as WebKitGTK # noqa
from .webkitgtk.options import Options as WebKitGTKOptions # noqa
from .remote.webdriver import WebDriver as Remote  # noqa
from .common.desired_capabilities import DesiredCapabilities  # noqa
from .common.action_chains import ActionChains  # noqa
from .common.touch_actions import TouchActions  # noqa
from .common.proxy import Proxy  # noqa
'''


class Firefox:
    def __init__(self):
        self.browser = None

    def create(self):
        self.browser = webdriver.Firefox(executable_path=os.path.join(BASE_DIR, 'webdriver/chromedriver'))


class Chrome:
    def __init__(self):
        self.browser = None

    def create(self):
        self.browser = webdriver.Chrome(executable_path=os.path.join(BASE_DIR, 'webdriver/chromedriver'))


class Phantomjs:
    def __init__(self):
        self.browser = None

    def create(self):
        self.browser = webdriver.PhantomJS(executable_path=os.path.join(BASE_DIR, 'webdriver/chromedriver'))

