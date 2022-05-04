# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 08:51
# @Author  : Walter
# @File    : readmysql.py
# @License : (C)Copyright Walter
# @Desc    :
import datetime
import json
from ZrLog接口测试框架.utils.mysqlutil import MysqlUtil

from ZrLog接口测试框架.utils.logutil import logger

mysql = MysqlUtil()

class RdTestcase:
    def load_all_case(self, web, module):
        sql = f"select * from `test_case_list` where web=\'{web}\' and module = \'{module}\'"
        results = mysql.get_fetchall(sql)
        return results

    def is_run_data(self, web, module):
        run_list = [case for case in self.load_all_case(web, module) if case['isdel'] == '1']
        return run_list

    def loadConfKey(self, web, key_values):
        sql = f"select * from `test_config` where web = \'{web}\' and key_values = \'{key_values}\'"
        results = mysql.get_fetchone(sql)
        return results

    def updateResults(self, response, is_pass, case_id):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = f"insert into `test_result_record` (case_id, times, response, result) values('{case_id}', '{current_time}', '{json.dumps(response, ensure_ascii=False)}','{is_pass}')"
        rows = mysql.sql_execute(sql)
        logger.debug(sql)
        return rows
if __name__ == '__main__':
    test = RdTestcase()
    res = test.updateResults({
        'code': 200,
        'cody': {'error': 1, 'message': '用户名和密码不能为空'},
        'cookies': {}
    }, 'True', '4565')
    print(res)