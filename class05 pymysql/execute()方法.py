# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 20:55
# @Author  : Walter
# @File    : execute()方法.py
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
# 删除数据
sql = "delete from log where alias='alias01'"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
cursor.close()
db.close()