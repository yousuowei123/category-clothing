# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

from download import get_page_source
from download import save_link_to_file
from pyquery import PyQuery as pq
import json
import os
from random import randint
from time import sleep

'''
  -*- 该脚本功能 -*-
用于获取衣服类别下面的所有子类别的链接
return层次一: 如{'Woman': 'Woman_url', 'Man': 'Man_url'......}

return层次二: 如{'Woman': [{'clothing': 'clothing_url', 'shoes':'shoes_url'...,
                'Man': [{'clothing': 'clothing_url', 'shoes': 'shoes_url'...}]}
'''

path = r'E:\My Work new\Amazon project\Amazon category\tmp table'


def parse_third_page_source(html):
    '''
    --> 解析第三层链接html中的(如女人的衣服中的裙子, 毛衣, 裤子)， 生成第四层需要的url
    :param html:
    :return: 第四层需要的url
    '''
    third_doc = pq(html)
    ul_item = third_doc("#leftNav")
    list_item = ul_item.find("ul.a-unordered-list.a-nostyle.a-vertical.a-spacing-base > ul > li > span > ul > div > li:first-child")
    print(list_item)
    print('6'*50)

    li_items = list_item.find("span > ul > div > li")
    third_url_list = []
    for li in li_items.items():
        a_url = 'https://www.amazon.com' + li.find('a').attr('href')
        print(a_url)
        third_url_list.append(a_url)

    return third_url_list


def parse_second_page_source_one(html, categories_name):
    '''
    --> 解析第二层链接的html中的(如女人中的衣服，鞋子...), 生成第三层需要的url
    情况为["Women", "Men", "Girls", "Boys"]时的解析方法
    :param html:
    :return: 第三层需要的url
    '''
    if html is None:
        return '获取网页失败'
    second_doc = pq(html)
    ul_items = second_doc("#leftNav ul").items()

    second_url_list = []
    category_dict = {}
    for ul in ul_items:
        list_a = []
        for all_a in ul.find('li span a').items():
            a_dict = {}
            a_name = all_a.find('span').text()
            a_url = 'https://www.amazon.com' + all_a.attr('href')
            a_dict[a_name] = a_url

            list_a.append(a_dict)
        second_url_list.append(list_a)

    if second_url_list:  # 转化成我们需要的格式，方便存储和整理
        second_url_list = second_url_list[-2:]
        category_dict[categories_name] = second_url_list[0]
        category_dict['shops'] = second_url_list[1]
        save_link_to_file(link_name='second_floor.txt', link_url= category_dict)
    else:
        print('触发了robot check')

    t = randint(1, 3)
    sleep(t)

    # link_name = 'second_floor_txt'
    # return second_url_list


def parse_second_page_source_two(html, categories_name):
    '''
    情况为["Baby", "Novelty & More", "Luggage & Travel Gear"]时的解析方法
    '''
    page_two_doc = pq(html)
    li_list_item = page_two_doc('#leftNav > ul > ul > li > span > ul > div > li')

    category_dict = {}
    second_url_list = []
    for li in li_list_item.items():
        a_dict = {}
        a_name = li.find('span > a > span').text()
        a_url = 'https://www.amazon.com' + li.find('span a').attr('href')
        a_dict[a_name] = a_url
        second_url_list.append(a_dict)

    category_dict[categories_name] = second_url_list
    save_link_to_file(link_name='second_floor.txt', link_url=category_dict)
    # print(category_dict)
    t = randint(1, 3)
    sleep(t)


def parse_second_page_source_three(html, categories_name):
    '''
    --> 情况为["Uniforms, Work & Safety", "Costumes & Accessories", \
    "Shoe, Jewelry & Watch Accessories"]时的解析方法
    '''
    page_three_doc = pq(html)
    if categories_name in ["Traditional & Cultural Wear"]:
        li_list_item = page_three_doc('#leftNav > ul:nth-child(3) > ul > li > span > ul > div > li')
    else:
        li_list_item = page_three_doc('#leftNav > ul:nth-child(6) > ul > li > span > ul > div > li')

    category_dict = {}
    second_url_list = []
    for li in li_list_item.items():
        a_dict = {}
        a_name = li.find('span > a > span').text()
        a_url = 'https://www.amazon.com' + li.find('span a').attr('href')
        a_dict[a_name] = a_url
        second_url_list.append(a_dict)

    category_dict[categories_name] = second_url_list
    save_link_to_file(link_name='second_floor.txt', link_url=category_dict)
    # print(category_dict)

    t = randint(1, 3)
    sleep(t)


def parse_first_page_source(html):
    '''
    --> 解析服装类第一层链接的html中的(女人，男人，女孩，男孩...)， 生成第二层需要的url
    :param html:
    :return: 第二层需要的url
    '''
    first_doc = pq(html)
    li_items = first_doc("#leftNav").find("li").items()
    for li in li_items:
        categories_dict = {}
        Categories_name = li.find('a h4').text()
        href = 'https://www.amazon.com' + li.find('a').attr('href')
        categories_dict['categories_name'] = Categories_name
        categories_dict['href'] = href
        save_link_to_file(link_name='first_floor.txt', link_url=categories_dict)


def main_first():
    '''
    --> 把第一层的html解析出来第二层的url并保存到first_url.txt文件中
    '''

    first_url = "https://www.amazon.com/amazon-fashion/b/ref=topnav_storetab_sl?ie=UTF8&node=7141123011"
    html = get_page_source(first_url)  # 获取网页的源代码
    print(html)
    parse_first_page_source(html)  # 剖析第一层html


def main_second():
    '''
    --> 从第二层url中解析出第三层的url并保存到second_url.txt文件中
    :return:
    '''
    file_name = 'first_floor.txt'
    file_path = os.path.join(path, file_name)
    file = open(file_path, encoding='utf-8')

    for per_column in file:
        try:
            url_dict = per_column.strip()
            url_item = json.loads(url_dict)
            categories_name = url_item['categories_name']
            url = url_item['href']
            # print(url)  测试通过
            html = get_page_source(url)
            print(html)
            if categories_name in ["Women", "Men", "Girls", "Boys"]:
                parse_second_page_source_one(html, categories_name)
            elif categories_name in ["Baby", "Novelty & More", "Luggage & Travel Gear"]:
                parse_second_page_source_two(html, categories_name)
            else:
                parse_second_page_source_three(html, categories_name)

        except Exception as e:
            print(e)
            continue

    file.close()


def test_case():
    '''
    --> 用于测试逻辑结果是否符合预期和是否发生异常
    '''
    test_url = 'https://www.amazon.com/s/ref=lp_7141123011_ex_n_8/143-3620478-1851336?rh=n%3A7141123011%2Cn%3A7586144011&bbn=7141123011&ie=UTF8'
    html = get_page_source(test_url)
    print(html)
    parse_second_page_source_three(html, 'Uniforms, Work & Safety')


if __name__ == "__main__":
    # main_first()  # 测试完成
    main_second()
    # test_case()


