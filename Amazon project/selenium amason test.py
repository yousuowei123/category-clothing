# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

from selenium import webdriver
import time

start_time = time.time()

# 使用chrome界面浏览器
chrome_executable_path = r"E:\Developer Tools\driver\chromedrivernew"
# browser = webdriver.Chrome(chrome_executable_path)

# 使用phantomjs浏览器
# file_path = r"E:\Developer Tools\driver\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs"
# browser = webdriver.PhantomJS(executable_path=file_path)  # phantomjs无头浏览器将被selenium弃用

# 创建的新实例驱动, 使用chrome-headless测试
options = webdriver.ChromeOptions()
options.add_argument('headless')
url = 'https://www.amazon.com/Champion-Freedom-Racerback-Pinksicle-X-Small/dp/B017UWLTEQ/ref=lp_1044990_1_10?s=apparel\
&ie=UTF8&qid=1518485586&sr=1-10&nodeID=1044990&psd=1'

browser = webdriver.Chrome(executable_path=chrome_executable_path, chrome_options=options)

browser.get(url)
time.sleep(5)
title = browser.find_element_by_css_selector("#productTitle")
print(title.text)
price = browser.find_element_by_css_selector("#priceblock_ourprice")
print(price.text)
user_time = time.time() - start_time
print("使用时间：{}".format(user_time))

browser.close()