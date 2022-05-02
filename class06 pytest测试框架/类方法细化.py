# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 11:34
# @Author  : Walter
# @File    : 类方法细化.py
# @License : (C)Copyright Walter
# @Desc    :

# 在类里面。运行顺序为：setup_class > setup_method > setup >用例> teardown > teardown_method > teardown_class
# 函数里面用到的setup/teardown_function与类里面的setup/teardown_class互不干涉，互不影响。

import pytest


class Test():
    def setup_method(self):
        print('setup_method')
    def teardown_method(self):
        print('teardown_method()')

    def setup(self):
        print('类方法细化setup')
    def teardown(self):
        print('类方法细化teardown')

    def test01(self):
        print('test01()')
    def test02(self):
        print('test02()')

if __name__ == '__main__':
    # v参数显示命令执行过程
    # s参数显示print打印信息
    pytest.main(['-v', '-s', '类方法细化.py'])