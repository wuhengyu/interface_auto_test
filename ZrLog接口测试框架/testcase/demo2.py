# -*- coding: utf-8 -*-
# @Time    : 2022/5/8 18:14
# @Author  : Walter
# @File    : demo2.py
# @License : (C)Copyright Walter
# @Desc    :
aa = {'body': {'data': {'version': 0, 'digest': '<p>测试内容</p>', 'thumbnail': None, 'logId': 78, 'rubbish': True, 'alias': '78'}, 'message': None, 'error': 0}, 'admin_token': ['1#4157736A624250425263344E366566626E63763957645672475239716F47772B52456E4D70734F34506C6B4265426C32702F6F53726762594445484B54564A354A616D4176316D56316E4E5A54553761324933577A7279627A73412F504878565642445438474C487950413D']}
print(type(aa))
print(aa['body']['data']['logId'])
bb = [88]
cc = dd = bb[0]
print(cc)

ee = {"keywords": "","rubbish": True,"title": "自动化测试1","markdown": "测试内容","content": "<p>测试内容</p>\n","typeId": 1}
ee['aaaa'] = '11111'
print(ee)

gg = 100
ggg = str(gg)
print(type(ggg))

sss = '{"keywords": "","rubbish": True, "title": "测试112233","typeId": 1,"version": 10,"digest": "<p>测试</p>", "thumbnail": "","markdown": "测试", "content": "<p>测试</p>\\n"}'
print(eval(sss))
