# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 18:02
# @Author  : Walter
# @File    : base.py
# @License : (C)Copyright Walter
# @Desc    :
import json
from string import Template
import re

def find(data):
    if isinstance(data, dict):
        data = json.dumps(data)
        pattern = "\\${(.*?)}"
        return re.findall(pattern, data)

def relace(ori_data, reolace_data):
    ori_data = json.dumps(ori_data)
    s = Template(ori_data)
    return s.safe_substitute(reolace_data)

def parse_relation(var, resdata):
    if not var:
        return resdata
    else:
        resdata = resdata.get(var[0])
        del var[0]
        return parse_relation((var, resdata))

if __name__ == '__main__':
    ori_data = {"admin-token": "${token}"}
    replace_data = {'token': 'x015k878'}
    print(ori_data, replace_data)