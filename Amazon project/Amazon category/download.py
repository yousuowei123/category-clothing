# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

import requests
from random import choice
import os
import json
from time import sleep
import random


'''
针对所有页面请求功能模块, amazon出触发Robot Check检查
'''

# 同一个浏览器头不能连续请求两次
headers_pool = [
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
    'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4482.400 QQBrowser/9.7.13001.400'
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    ]


def get_page_source(url, proxies=None, num_retries=3):
    '''
    定制用于请求网页源代码封装好的模块
    '''
    print("\033[32;1mdownload\033[0m: {}".format(url))
    headers = {"user-agent": choice(headers_pool),
               'Accept - Encoding': 'gzip, deflate, br',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Host': 'www.amazon.com'
               }
    # proxies = {
    #     'http': 'http://121.31.177.224:8123',
    #     'https': 'https://121.31.177.224:8123'
    #
    # }

    try:
        if proxies is not None:
            r = requests.get(url, headers=headers, proxies=proxies, timeout=20)
        else:
            r = requests.get(url, headers=headers, timeout=10)
            r.encoding = "utf-8"
        if r.status_code == 200:
            return r.text
        elif r.status_code == 503:
            t = random.randint(1, 3)
            sleep(t)
            return get_page_source(url)

    except requests.exceptions.Timeout:
        print('连接超时，请重试')
        t = random.randint(1, 3)
        sleep(t)
        return get_page_source(url)

    except Exception as e:
        print(e)
        if num_retries > 0:
            print("尝试重连倒数第{}次".format(num_retries-1))
            return get_page_source(url, num_retries-1)
        return None


def save_link_to_file(link_name=None, link_url=None):
    '''
    用于保存文件封装好的模块
    '''
    path = r'E:\My Work new\Amazon project\Amazon category\tmp table'
    file_name = os.path.join(path, link_name)

    with open(file_name, 'a', encoding='utf-8') as f:
        if isinstance(link_url, dict):
            link_url = json.dumps(link_url, ensure_ascii=False) + '\n'
            print("\033[31;1m网址字典保存成功\033[0m", link_url)
            f.write(link_url)
            f.close()
        else:
            f.write(link_url + '\n')
            print("\033[31;1m网址保存成功\033[0m", link_url)
            f.close()


if __name__ == "__main__":
    # link_name = "123.txt"
    # link_url = "https://www.baidu.com"
    # save_link_to_file(link_name, link_url)
    # print(len(headers_pool))
    pass


