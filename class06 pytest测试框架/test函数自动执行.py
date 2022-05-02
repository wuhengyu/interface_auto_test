# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 22:04
# @Author  : Walter
# @File    : test函数自动执行.py
# @License : (C)Copyright Walter
# @Desc    :

import pytest

print('test开头会被执行')

def test_login():
    print('test_login')

def testlogin():
    print('testlogin')

def logintest():
    print('logintest')

def login_test():
    print('login_test')

def logintesting():
    print('logintesting')

if __name__ == '__main__':
    # v参数显示命令执行过程
    # s参数显示print打印信息
    pytest.main(['-s', '-v', 'test函数自动执行.py'])