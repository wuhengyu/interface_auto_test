# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 09:55
# @Author  : Walter
# @File    : setup和teardown方法.py
# @License : (C)Copyright Walter
# @Desc    :

import pytest

# 模块级别，每个模块都执行一次setup_module()和teardown_module()，全局中
def setup_module():
    print('setup_module()')
def teardown_module():
    print('teardown_module()')
def test01():
    print('test01()')
def test02():
    print('test02()')

# 函数级别，每个函数级别用例执行前后执行一次setup_function()和teardown_function()，不在类中
def setup_function():
    print('setup_function()')
def teardown_function():
    print('teardown_function()')
def test03():
    print('test03()')
def test04():
    print('test04()')

# 类级别，每个类中方法执行前后执行一次setup_class()和teardown_class()，在类中
class Test01:
    def setup_class(self):
        print('setup_class()')
    def teardown_class(self):
        print('teardown_class()')
    def test05(self):
        print('test05()')
    def test06(self):
        print('test06()')

# 类方法级别，每个方法执行前后执行一次setup_method()和teardown_method()，在类中
class Test02():
    def setup_method(self):
        print('setup_method()')
    def teardown_method(self):
        print('teardown_method()')
    def test06(self):
        print('test06()')
    def test07(self):
        print('test07()')

if __name__ == '__main__':
    # v参数显示命令执行过程
    # s参数显示print打印信息
    pytest.main(['-s', '-v', 'setup和teardown方法.py'])

