# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 15:25
# @Author  : Walter
# @File    : fetchone方法.py
# @License : (C)Copyright Walter
# @Desc    :

import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='ZrLog',
    charset='utf8',
    port=3306
)
cursor = db.cursor()
sql = "select * from log"
cursor.execute(sql)
# 一次性获取一条元组记录
res = cursor.fetchone()
print(res)
cursor.close()
db.close()
