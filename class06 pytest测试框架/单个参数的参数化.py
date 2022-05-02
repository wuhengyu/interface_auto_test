# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 22:32
# @Author  : Walter
# @File    : 单个参数的参数化.py
# @License : (C)Copyright Walter
# @Desc    :

import pytest

# parametrize(参数名，参数值)，单个参数名，参数值是列表类型，列表当中包含字符串，元组，字典对象

@pytest.mark.parametrize("username", ["ceshi1", "ceshi2", "ceshi3"])
def test_login1(username):
    print(f'字符串参数化：{username}')

@pytest.mark.parametrize("numbers", [(1,2), (3, 4), (5, 6)])
def test_login2(numbers):
    print(f'元组参数化：{numbers}')

@pytest.mark.parametrize("register", [{"name":"zhangsan"}, {"password", "123456"}])
def test_login3(register):
    print(f'字典参数化：{register}')

if __name__ == '__main__':
    # v参数显示命令执行过程
    # s参数显示print打印信息
    pytest.main(['-s', '-v', '单个参数的参数化.py'])
