# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 22:30
# @Author  : Walter
# @File    : 方法的执行规则.py
# @License : (C)Copyright Walter
# @Desc    :

import pytest

class TestOrdering:
    def test_login(self):
        print('test_login')

    def testlogin(self):
        print('testlogin')

    def logintest(self):
        print('logintest')

    def login_test(self):
        print('login_test')

    def logintesting(self):
        print('logintesting')

if __name__ == '__main__':
    # v参数显示命令执行过程
    # s参数显示print打印信息
    pytest.main(['-s', '-v', '方法的执行规则.py'])