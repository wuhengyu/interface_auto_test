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

dic={'abc':123,'aaa':333,'wer':334}
def text_dic(**dd):
    for a,b in dd.items():# a 代表键 ，b代表值
        print(a,b)
    for xin in dd.items():# a 代表键 ，b代表值
        print(list(xin))
        print(tuple(xin))
    for xin in dd.values():# a 代表键 ，b代表值
        print(xin)
    for xin in dd.keys():# a 代表键 ，b代表值
        print(xin)
text_dic(**dic)


aaa = '{"userName": "admin","password": 123456,"https": False,"key": 1598188173501}'
bbb = '{"userName": "admin","password": 123456,"https": "False","key": 1598188173501}'

print(eval(aaa))
print(json.loads(bbb))
print(json.loads(json.dumps(aaa)))
print(json.dumps(aaa))

# ccc = {"userName": "admin","password": 123456,"https": False,"key": 1598188173501}
# print(type(ccc))
# print(eval(ccc))

try:
    assert 1 == 1
    print('222')
except:
    print('111')