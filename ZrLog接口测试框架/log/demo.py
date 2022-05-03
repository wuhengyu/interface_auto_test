# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 14:43
# @Author  : Walter
# @File    : demo.py
# @License : (C)Copyright Walter
# @Desc    :
import datetime
import time

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'), time.localtime()))
print('aa_{}'.format(time.strftime('%Y-%m-%d %H:%M:%S'), time.localtime()))
