# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 11:56
# @Author  : Walter
# @File    : demo2.py
# @License : (C)Copyright Walter
# @Desc    :

import pytest


def setup_module():
    print("模块开始时，执行setup_module")


def teardown_module():
    print("模块结束时，执行teardown_module")


def setup_function():
    print("函数用例开始时，执行setup_function")


def teardown_function():
    print("函数用例结束时，执行teardown_function")


def test_a():
    print("执行测试函数a")


def test_b():
    print("执行测试函数b")


class TestDemo(object):
    def setup_class(self):
        print("测试类开始时，执行setup_class")

    def teardown_class(self):
        print("测试类结束时，执行teardown_class")

    def setup_method(self):
        print("类中的方法开始时，执行setup_method")

    def teardown_method(self):
        print("类中的方法结束时，执行teardown_method")

    def test_case1(self):
        print("执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("执行测试用例2")
        assert 1 + 3 == 4

    def test_case3(self):
        print("执行测试用例3")
        assert 1 + 5 == 6
