# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

import requests
import re
from bs4 import BeautifulSoup
import time
from random import choice

# session = requests.Session()
headers_pool = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
    'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
    'Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5',
    'Mozilla/5.0(Linux;U;Android2.3.7;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1'
    ]


def get_page_source(url):
    print("\033[32;1mdownload:{}\033[0m".format(url))
    try:
        # params = {
        #     's': 'apparel',
        #     'ie': 'UTF8',
        #     'qid': 1518485586,
        #     'sr': '1 - 10',
        #     'nodeID': 1044990,
        #     'psd': 1
        # }
        headers = {
            'User-Agent': choice(headers_pool)
        }
        proxies = {
            'http': 'http://125.108.40.213:61202',
            'https:': 'https://14.29.47.90:3128'
        }

        r = requests.get(url, headers=headers, proxies=proxies, timeout=15)
        r.raise_for_status()
        r.encoding = 'utf-8'

    except Exception as e:
        print(e)
        return None
    else:
        return r.text


def parse_one_goods_detail(html):
    product_title = re.findall('<span.*?id="productTitle".*?class=.*?>(.*?)</span>', html, re.S)
    if product_title:
        product_title = product_title[0].strip()
    else:
        product_title = ''

    # selling_point_big = re.findall('<ul class="a-unordered-list a-vertical a-spacing-none">.*?</span></li>', html, re.S)
    # soup = BeautifulSoup(html, 'lxml')
    # detailBullets_feature_div = soup.find(attrs={'id':re.compile("detailBullets_feature_div")})
    # list_item_property = detailBullets_feature_div.find_all(class_="a-list-item")
    # details = re.findall('<div id="productDescription" class="a-section a-spacing-small">(.*?)</div>', html, re.S)
    # A_plus = re.findall('<div class="aplus-v2 desktop celwidget" cel_widget_id="aplus">(.*?)</div>.*', html, re.S)
    print(product_title)


if __name__ == "__main__":
    url = 'https://www.amazon.com/Champion-Freedom-Racerback-Pinksicle-X-Small/dp/B017UWLTEQ/ref=lp_1044990_1_10'
    html = get_page_source(url)
    print(html)
    print('-'*50)
    parse_one_goods_detail(html)


