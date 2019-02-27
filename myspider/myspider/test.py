#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import sys
import os
import time
from myspider.downloaders import myselenium
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    browser = myselenium.load_firefox(load_images=False,display=False)
    browser.get('https://blog.csdn.net/lbxoqy/article/details/70052375')
    browser.get_screenshot_as_file('screensoot.png')
    # time.sleep(10)
    browser.close()
    # time.sleep(10)
    # browser.quit()
