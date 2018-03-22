# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

import json
import os

'''
  -*- 该脚本功能 -*-
用于存储把类目列表存储到同一个文件中，并且区分列表类别字段内容如
(0: 表示全列表， 1:表示有嵌入其他商品的列表) --> 方便之后爬取列表统一调用
'''

path = r'E:\My Work new\Amazon project\Amazon category\tmp table'
file_name = 'category list.txt'
path_name = os.path.join(path, file_name)


def store_category_list(content):
    '''
    :param content: dict
    :return: None
    '''
    with open(path_name, 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        print('\033[32;1murl_list存储成功\033[0m', content)

        f.close()

