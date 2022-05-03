# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 00:08
# @Author  : Walter
# @File    : mysqlutil.py
# @License : (C)Copyright Walter
# @Desc    :

import pymysql

from ZrLog接口测试框架.config.setting import DB_CONFIG
from ZrLog接口测试框架.log.logutil import logger

class MysqlUtil:
    def __init__(self):
        self.db = pymysql.connect(**DB_CONFIG)
        # cursor=pymysql.cursors.DictCursor 设置返回值为字典
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def get_fetchone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_fetchall(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def sql_execute(self, sql):
        try:
            if self.db and self.cursor:
                self.cursor.execute(sql)
                self.db.commit()
        except Exception as e:
            self.db.rollback()
            logger.error('sql执行错误，已执行回滚')
        return 0

    def close(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.db is not None:
            self.db.close()

if __name__ == '__main__':
    mysql = MysqlUtil()
    res = mysql.get_fetchall('select * from test_case_list')
    print(res)

