# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 12:13
# @Author  : Walter
# @File    : test_01.py
# @License : (C)Copyright Walter
# @Desc    :
import pytest

class TestClass01:
    def test_login(self):
            print("test_login")
#
# def testlogin():
#     print("testlogin")

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_01.py'])