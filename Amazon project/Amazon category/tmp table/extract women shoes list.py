# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

import os
import json
from download import get_page_source
from pyquery import PyQuery as pq
from save_category_list import store_category_list
from download import save_link_to_file


'''
    -*- 该脚本功能 -*-
    代码结构和extract women clothing一致，需修改相关参数
为了获取Woman或者和Woman相同网页结构(Shoes和Watches)的所有类目list
特殊形式 --> {'category_levels': 'Woman:Clothing:dresses:...', 
            'category_list_url': 'url', 'category_class': 0} --> 还可能混有其他的list
一般形式 --> {'category_levels': 'Woman:Clothing:dresses:...', 
            'category_list_url': 'url', 'category_class': 1} --> 纯页面的list
'''

path = r'E:\My Work new\Amazon project\Amazon category\tmp table'


def open_second_floor_file():
    '''
    get_cate_url() --> 读取第二层文件中的url到list中
    '''
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


def get_women_class():
    '''
    获取女人类所有的衣服种类
    :return:a dict like this {'item_name': 'Clothing', 'item_url': 'url'}
    '''
    results = open_second_floor_file()
    women_url_list = results[0].get("Women")
    women_shops_list = results[0].get('shops')

    item_list = []
    for item in women_url_list:
        item_dict = {}
        for key, value in item.items():
            item_name = key
            item_url = value
            item_dict['item_name'] = item_name
            item_dict['item_url'] = item_url
        item_list.append(item_dict)  # 输出了两个参数

    return item_list

# 上面的两个函数主要用于主函数的调用


def parse_clothing_child_page(html=None, clothing_name=None):
    '''
    同样适用shoes, Watches,
    parse_clothing_child_page(html) --> 解析衣服页面的html
    :param clothing_name: Women:Clothing
    return: 如[{'name': 'Women:Clothing:Dresses', 'href':'url'}, {'name': 'Women:Clothing:sweater', 'href':url},...]
    '''
    clothing_doc = pq(html)
    ul_item = clothing_doc('#leftNav > ul.a-unordered-list.a-nostyle.a-vertical.a-spacing-base')
    span_item = ul_item.find('ul > li > span')
    span_list_item = span_item.find('div > li > span')
    li_list_item = span_list_item.find('ul.a-unordered-list.a-nostyle.a-vertical.s-ref-indent-one > div > li')
    # print(li_list_item)

    item_list = []
    for li_item in li_list_item.items():
        clothing_dict = {}
        child_name = li_item.find('span > a > span').text()
        child_href = 'https://www.amazon.com' + li_item.find('span > a').attr('href')
        clothing_dict['name'] = "{}:{}".format(clothing_name, child_name)
        clothing_dict['href'] = child_href
        item_list.append(clothing_dict)

    # print(item_list)
    return item_list


def parse_dresses_level_child_page(html=None, parent_name=None):
    '''
    解析裙子或和裙子网页结构相似的页面
    :param parent_name: Women:Clothing:Dresses
    :return: [{'child_name': 'Women:Clothing:Dresses:Casual',...}]
    '''
    clothing_doc = pq(html)
    ul_item = clothing_doc('#leftNav > ul.a-unordered-list.a-nostyle.a-vertical.a-spacing-base')
    span_item = ul_item.find('ul > li > span')
    span_list_item = span_item.find('div > li > span')
    li_item = span_list_item.find('ul.a-unordered-list.a-nostyle.a-vertical.s-ref-indent-one > div > li')
    # print(li_item)
    li_list_item = li_item.find('ul.a-unordered-list.a-nostyle.a-vertical.s-ref-indent-one > div > li')
    print(li_list_item)
    print('-'*60)

    li_item_list = []
    for li_item in li_list_item.items():
        dresses_dict = {}
        child_name = li_item.find('span > a > span').text()
        child_href = 'https://www.amazon.com' + li_item.find('span > a').attr('href')
        if child_name in ['Lingerie', 'Sleep & Lounge', 'Thermal Underwear',
                          'Bikinis', 'Tankinis', 'One-Pieces', 'Cover-Ups',
                          'Board Shorts', 'Racing', 'Rash Guards',
                          'Down & Parkas', 'Wool & Pea Coats', 'Trench, Rain & Anoraks',
                          'Quilted Lightweight Jackets', 'Casual Jackets', 'Denim Jackets',
                          'Leather & Faux Leather', 'Fur & Faux Fur', 'Vests', 'Active & Performance']:

            dresses_dict['category_levels'] = "{}:{}".format(parent_name, child_name)
            dresses_dict['category_url'] = child_href
            save_link_to_file('clothing_fifth_floor.txt', dresses_dict)
            li_item_list.append(dresses_dict)
        else:
            dresses_dict['category_class'] = 1
            dresses_dict['category_levels'] = "{}:{}".format(parent_name, child_name)
            dresses_dict['category_url'] = child_href
            store_category_list(dresses_dict)
            li_item_list.append(dresses_dict)

    print('-'*60)
    print(li_item_list)
    return li_item_list


def get_dresses_level_child_url_list(dresses_level_url=None, dresses_level_name=None):
    '''
    获取裙子或者裙子级别相同的所有类目list
    :param: dresses_level_name: Women:Clothing:Dresses
    '''
    # dresses_url = 'https://www.amazon.com/s/ref=lp_1040660_ex_n_3/143-8365897-7769519?rh=n%3A7141123011%2Cn%3A7147440011%2Cn%3A1040660%2Cn%3A1045024&bbn=1040660&ie=UTF8'
    html = get_page_source(dresses_level_url)
    print('-'*60)
    parse_dresses_level_child_page(html, dresses_level_name)


def get_clothing_child_url(clothing_name=None, clothing_url=None):
    '''
    同样适用shoes, Watches,
    get_clothing_child_url(clothing_url=None) --> 获取衣服类下面所有的子类url
    :param: clothing_name: Women:Clothing
    :return: url 组成的list
    '''
    # url = "https://www.amazon.com/s/ref=lp_7147440011_ex_n_2?rh=n%3A7141123011%2Cn%3A7147440011%2Cn%3A1040660&bbn=7147440011&ie=UTF8"
    html = get_page_source(clothing_url)
    # print(html)
    print('-'*60)
    results = parse_clothing_child_page(html, clothing_name)  # 是一个list
    for clothing_child in results:
        clothing_child_dict = {}
        if clothing_child['name'] in ["Women:Clothing:Fashion Hoodies & Sweatshirts", "Women:Clothing:Jeans",
                                      "Women:Clothing:Leggings", "Women:Clothing:Jumpsuits, Rompers & Overalls"]:
            clothing_child_dict["category_class"] = 0
            clothing_child_dict["category_levels"] = clothing_child['name']
            clothing_child_dict["category_url"] = clothing_child['href']
            store_category_list(clothing_child_dict)
        else:
            # pass
            dresses_level_name = clothing_child['name']
            dresses_level_url = clothing_child['href']
            print('获取第四层连接：', dresses_level_url)
            print('-'*60)
            get_dresses_level_child_url_list(dresses_level_url, dresses_level_name)


def get_clothing_url_list(clothing_name=None, clothing_url=None):
    '''
    获取clothing类下所有的list
    :param parent_name: Women:Clothing
    :param parent_url: Clothing对应的url
    :return: list
    '''
    get_clothing_child_url(clothing_name, clothing_url)


def get_first_class_url_list(parent_name=None, parent_url=None):
    '''
    --> 获取第一类的url_list
    :param parent_name: Women:Clothing、Women:Shoes和 Women:Watches
    :param parent_url: Clothing, Shoes和Watches对应的url
    :return: list
    '''

    parent_name = 'Women:Clothing'  # 该名字只是用于测试"{}:{}".format('Women', parent_name)
    parent_url = 'https://www.amazon.com/s/ref=lp_7147440011_ex_n_2/138-0803461-4666661?rh=n%3A7141123011%2Cn%3A7147440011%2Cn%3A1040660&bbn=7147440011&ie=UTF8'
    get_clothing_url_list(parent_name, parent_url)


def get_second_class_url_list(parent_name=None, parent_url=None):
    '''
    --> 获取第二类的url_list
    :param parent_name: Jewelry、Handbags & Wallets和 Accessories
    :param parent_url: Jewelry、Handbags & Wallets和 Accessories对应的url
    :return: list
    '''
    pass


def main():
    '''
    主调用函数
    '''
    for items in get_women_class():
        parent_name = items['item_name']
        parent_url = items['item_url']
        if parent_name in ['Clothing', 'Shoes', 'Watches']:
            parent_name = 'Women:{}'.format(parent_name)
            print('\033[32;1m我的name是:{}, 我是1类\033[0m'.format(parent_name))
            get_first_class_url_list(parent_name, parent_url)
        else:
            parent_name = 'Women:{}'.format(parent_name)
            print('\033[31;1m我的name是:{}, 我是2类\033[0m'.format(parent_name))
            # get_second_class_url_list(parent_name, parent_url)


if __name__ == "__main__":
    # get_clothing_child_url()  # 调试衣服页面
    # get_dresses_child_url()  # 调试裙子页面
    # get_women_class()  # 调试获取女人下的类
    # main()
    get_first_class_url_list()  # 调试第一种情况


