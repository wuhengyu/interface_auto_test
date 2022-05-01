# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 19:55
# @Author  : Walter
# @File    : rollback()方法.py
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
sql01 = "insert into log set logid=13,title='title01', alias='alias01', content='content01'"
sql02 = "insert into log set logid=14,title='title02', alias='alias02', content='content02'"

try:
    cursor.execute(sql01)
    cursor.execute(sql02)
    db.commit()
except:
    # sql02 logid重复回滚
    db.rollback()
cursor.close()
db.close()