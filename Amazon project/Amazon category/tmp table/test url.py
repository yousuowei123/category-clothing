# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

import os
import json

path = os.getcwd()
file_name = 'second_floor.txt'
file_path = os.path.join(path, file_name)

f = open(file_path, 'r')
f_content = f.read()
f_json = json.loads(f_content)
print(f_content)
if 'name' in f_json.keys():
    url_list = f_json.get('name')
    for url in url_list:
        print(url)

f.close()