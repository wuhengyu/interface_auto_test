# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 11:53
# @Author  : Walter
# @File    : test_02.py
# @License : (C)Copyright Walter
# @Desc    :
# file_name: test_fixtclass.py

import pytest


class TestClass:

    def setup(self):
        print("setup：每个用例执行前调用一次")

    def teardown(self):
        print("teardown：每个用例执行后调用一次")

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之后")

    def setup_method(self):
        print("setup_method：每个用例执行前调用一次")

    def teardown_method(self):
        print("teardown_method：每个用例执行后调用一次")

    def test_one(self):
        print("正在执行 test_one")
        a = "hello"
        b = "hello world"
        assert a in b

    def test_two(self):
        print("正在执行 test_two")
        a = "hello"
        assert hasattr(a, "check")

    def test_three(self):
        print("正在执行 test_three")
        a = "hello"
        b = "hello world"
        assert a == b


if __name__ == '__main__':
    pytest.main(['-s', 'test_02.py'])