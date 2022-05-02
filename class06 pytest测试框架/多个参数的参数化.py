# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 22:48
# @Author  : Walter
# @File    : 多个参数的参数化.py
# @License : (C)Copyright Walter
# @Desc    :

import pytest


# parametrize(参数名，参数值)，单个参数名，参数值是列表类型，列表当中包含字符串，元组，字典对象

@pytest.mark.parametrize("username1", ["ceshi1", "ceshi2", "ceshi3"])
@pytest.mark.parametrize("username2", ["ceshi11", "ceshi22", "ceshi33"])
def test_login1(username1, username2):
    print(f'第一个字符串参数化：{username1}, 第二个字符串参数化：{username2}')


@pytest.mark.parametrize("numbers1", [(1, 2), (3, 4), (5, 6)])
@pytest.mark.parametrize("numbers2", [(11, 22), (33, 44), (55, 66)])
def test_login2(numbers1, numbers2):
    print(f'第一个元组参数化：{numbers1}, 第二个元组参数化：{numbers2}')


@pytest.mark.parametrize("register1", [{"name1": "zhangsan1"}, {"password1", "123456"}])
@pytest.mark.parametrize("register2", [{"name2": "zhangsan2"}, {"password2", "123456"}])
def test_login3(register1, register2):
    print(f'第一个字典参数化：{register1}， 第二个字典参数化：{register2}')


if __name__ == '__main__':
    # v参数显示命令执行过程
    # s参数显示print打印信息
    pytest.main(['-s', '-v', '多个参数的参数化.py'])
