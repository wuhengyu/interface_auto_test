# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 19:07
# @Author  : Walter
# @File    : fetchmany方法.py
# @License : (C)Copyright Walter
# @Desc    :
import pymysql

db = pymysql.Connect(
    host='localhost',
    user='root',
    password='123456',
    database='ZrLog',
    charset='utf8',
    port=3306
)

cursor = db.cursor()
sql = 'select * from log'
cursor.execute(sql)
# 获取10条数据
res = cursor.fetchmany(10)
print(res)
cursor.close()
db.close()