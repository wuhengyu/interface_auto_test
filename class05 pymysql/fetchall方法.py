# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 19:16
# @Author  : Walter
# @File    : fetchall方法.py
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
# 获取全部数据
res = cursor.fetchall()
print(res)
cursor.close()
db.close()