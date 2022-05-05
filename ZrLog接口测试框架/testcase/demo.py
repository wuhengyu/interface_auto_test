# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 09:54
# @Author  : Walter
# @File    : demo.py
# @License : (C)Copyright Walter
# @Desc    :
import json
from ZrLog接口测试框架.utils.readmysql import RdTestcase

# print(eval('{"name": "1111"}'))
# print(json.loads('{"name": "1111"}'))

case_data = RdTestcase()
case_list2 = case_data.is_run_data('zrlog', '登录模块')

# print(case_data.loadConfKey('zrlog', 'url_api')['value'])
# print(case_list2)
# for _ in case_list2:
#     print(_['url'])


# for _ in case_list2:
#     url = case_data.loadConfKey('zrlog', 'url_api')['value']
#     api_url = _['url']
#     url = url + api_url
#     print(url)

# print(case_data.loadConfKey('zrlog', 'url_api')['value'] + case_list2['url'])
# url = case_data.loadConfKey('zrlog', 'url_api')['value'] + case_list2['url']

for _ in case_list2:
    method = _['method']
    print(method)

if 0 == 0:
    print('1111')