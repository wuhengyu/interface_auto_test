# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 14:43
# @Author  : Walter
# @File    : demo.py
# @License : (C)Copyright Walter
# @Desc    :
import datetime
import json
import time

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'), time.localtime()))
print('aa_{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'), time.localtime()))
print(time.localtime())

aaa = '111'
print('测试''aaa')
print('测试' + 'aaa')
print('%s' %('aaa'))

a = ['1']
print(str(a))
print(a[0])
print(''.join(a))
bb={'id': 8, 'web': 'zrlog', 'module': '文章管理模块', 'title': '发布文章', 'url': '/api/admin/article/create', 'method': 'post', 'headers': '{"Content-Type":"application/json"}', 'cookies': '{}', 'request_body': '{"keywords": "","rubbish": True,"title": "自动化测试1","markdown": "测试内容","content": "<p>测试内容</p>\\n","typeId": 1}', 'request_type': 'json', 'relation': 'id_name=body.id,alias_name=body.alias', 'expected_code': 'O', 'isdel': '1'}
print(bb['request_body'])
print(eval(bb['request_body']))
print(bb['title'])
# print(eval(bb['title']))

cc = {"aa":"111"}
print(cc['aa'])

dd = {'id': 8, 'web': 'zrlog', 'module': '文章管理模块', 'title': '发布文章', 'url': '/api/admin/article/create', 'method': 'post', 'headers': '{"Content-Type":"application/json"}', 'cookies': '{}', 'request_body': '{"keywords": "","rubbish": True,"title": "自动化测试1","markdown": "测试内容","content": "<p>测试内容</p>\\n","typeId": 1}', 'request_type': 'json', 'relation': 'id_name=body.id,alias_name=body.alias', 'expected_code': 'O', 'isdel': '1'}

print(type(dd['expected_code']))
print(dd['expected_code'])
# print(int(dd['expected_code']))

ee = 'O'
print(ee)
# print(int(ee))

# gg = 'O'
# print(int(gg))
