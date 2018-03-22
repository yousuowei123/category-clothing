# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

import os
import json
from download import get_page_source
from pyquery import PyQuery as pq


path = r'E:\My Work new\Amazon project\Amazon category\tmp table'


def get_cate_url():
    file_name = "second_floor.txt"
    file_path = os.path.join(path, file_name)
    f = open(file_path, 'r', encoding='utf-8')
    cate_list = []
    for file in f:
        cate_element = json.loads(file.strip())
        cate_list.append(cate_element)
        # print(cate_element)

    f.close()
    return cate_list


def parse_clothing_child_page(html):
    clothing_doc = pq(html)
    li_list_item = clothing_doc.find('#leftNav > ul.a-unordered-list.a-nostyle.a-vertical.a-spacing-base > ul > li > span > ul > div > li:nth-child(2) > span > ul > div > li')
    print(li_list_item)
    for li_item in li_list_item.items():
        name = li_item.find('span > a > span').text()
        href = 'https://www.amazon.com' + li_item.find('span > a').attr('href')
        print(name, href)


def get_clothing_child_url(clothing_url=None):
    url = "https://www.amazon.com/s/ref=lp_7147440011_ex_n_2?rh=n%3A7141123011%2Cn%3A7147440011%2Cn%3A1040660&bbn=7147440011&ie=UTF8"
    html = get_page_source(url)
    # print(html)
    parse_clothing_child_page(html)


def main():
    results = get_cate_url()
    woman_url_list = results[0].get("Women")
    woman_shops_list = results[0].get('shops')
    for item in woman_url_list:
        print(item)


if __name__ == "__main__":
    get_clothing_child_url()




