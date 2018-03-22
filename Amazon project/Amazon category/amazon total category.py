# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

import requests
from random import choice
from bs4 import BeautifulSoup
import re
import json


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


def get_page_source(url, num_retries=3):
    print("\033[32;1mdownload\033[0m: {}".format(url))
    headers = {"user-agent": choice(headers_pool)}
    proxies = {
        'https': 'https://121.31.177.224:8123',
        # 'https': 'https://219.135.164.245:3128'
        # 'https': 'https://114.113.126.82:80'
    }

    try:
        r = requests.get(url, headers=headers, proxies=proxies, timeout=10)
        r.raise_for_status()
        r.encoding = "utf-8"

    except Exception as e:
        print(e)
        if num_retries > 0:
            print("尝试重连第{}次".format(num_retries-2))
            return get_page_source(url, num_retries-1)
        return None
    else:
        num_retries = 3
        return r.text


def parse_total_page(html):
    soup = BeautifulSoup(html, "lxml")
    containers = soup.find_all(attrs={'class': re.compile('a-column a-span3 fsdColumn fsdColumn_3')})
    # print('所有的containers', containers)
    for container in containers:
        # print(container)
        fsdDeptBoxes = container.find_all(attrs={'class': re.compile('fsdDeptBox')})
        for fsdDeptBox in fsdDeptBoxes:
            parents_title = fsdDeptBox.find(attrs={'class': "fsdDeptTitle"}).get_text()
            all_a = fsdDeptBox.find_all(attrs={'class': 'a-link-normal fsdLink fsdDeptLink'})
            a_list = []
            for a in all_a:
                a_dict = {}
                a_title = a.get_text()
                a_href = a.attrs['href']
                if 'node=' in a_href:
                    id = eval(a_href.split("node=")[-1])
                else:
                    id = " "

                a_dict['child_id'] = id
                a_dict['child_title'] = a_title
                a_dict['child_href'] = "https://www.amazon.com" + a_href
                a_list.append(a_dict)

            yield{
                parents_title: a_list
            }

            print(parents_title, a_list)
            print('-'*50)


def save_to_file(content):
    with open('total_category.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        print('保存成功', content)
        f.close()


def main():
    url = "https://www.amazon.com/gp/site-directory/ref=nav_shopall_fullstore"
    html = get_page_source(url)
    print(html)
    for item in parse_total_page(html):
        save_to_file(item)


if __name__ == "__main__":
    main()