# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 12:57
# @Author  : Walter
# @File    : setting.py
# @License : (C)Copyright Walter
# @Desc    :
import os.path

abs_path = os.path.abspath(__file__)
# print(abs_path)
project_path = os.path.dirname(os.path.dirname(abs_path))
# print(project_path)
_conf_path = project_path + os.sep + 'config'
# print(_conf_path)
# 或者
# print(os.path.dirname(abs_path))

_log_path = project_path + os.sep + 'log'
_report_path = project_path + os.sep + 'report'
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "123456",
    "port": 3306,
    "database": "test",
    "charset": "utf8"
}

def get_log_path():
    return _log_path

def get_report_path():
    return _report_path

def get_conf_path():
    return _conf_path

class DynamicOaram:
    pass

if __name__ == '__main__':
    print(get_log_path())