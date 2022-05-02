# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 23:03
# @Author  : Walter
# @File    : assert原生断言.py
# @License : (C)Copyright Walter
# @Desc    :

import pytest

x = 1
y = 'on'
z = 'python'
w = 'python'

# 真pass
def test_int_001():
    assert x
# 不为真failed
def test_int_002():
    assert not x
# 包含pass
def test_int_003():
    assert y in z
# 包含failed
def test_int_004():
    assert z in y
# 等于pass
def test_int_005():
    assert z == w
# 等于failed
def test_int_006():
    assert z == x
# 不等于pass
def test_int_007():
    assert z != x
# 不等于failed
def test_int_008():
    assert z != w


if __name__ == '__main__':
    # v参数显示命令执行过程
    # s参数显示print打印信息
    pytest.main(['-s', '-v', 'assert原生断言.py'])
