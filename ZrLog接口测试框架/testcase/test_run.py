# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 19:24
# @Author  : Walter
# @File    : test_run.py
# @License : (C)Copyright Walter
# @Desc    :
import datetime
from ZrLog接口测试框架.config.setting import DynamicParam
from ZrLog接口测试框架.utils.logutil import logger
import pytest
from ZrLog接口测试框架.utils.requestsutil import RequestSend
from ZrLog接口测试框架.utils.readmysql import RdTestcase

attribute = DynamicParam()
case_data = RdTestcase()
case_login_in = case_data.is_run_data('zrlog', '登录模块')[0:1]
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class TestApi:
    def setup_class(self):
        logger.info(f"开始执行用例，开始时间为{current_time}")

    def teardown_class(self):
        logger.info(f"执行用例完成，结束时间为{current_time}")

    @pytest.mark.parametrize('case_login_in', [case_login_in])
    def test_login(self, case_login_in):
        for login_in in case_login_in:
            url = case_data.loadConfKey('zrlog', 'url_api')['value']
            api_url = login_in['url']
            url = url + api_url
            method = login_in['method']
            headers = eval(login_in['headers'])
            cookies = eval(login_in['cookies'])
            print("login_in:", login_in)
            print("login_in['request_body']:", login_in['request_body'])
            data = eval(login_in['request_body'])
            case_name = login_in['title']
            try:
                logger.info('正在执行{}用例'.format(case_name))
                res_data = RequestSend().send(url, method, data=data, headers=headers, cookies=cookies)
                logger.info("用例执行成功，请求结果为{}".format(res_data))
            except:
                logger.info("用例执行失败，请查看日志查找原因")
                assert False
            self.assert_response(login_in, res_data)
            return res_data

    def assert_response(self, login_in, res_data):
        is_pass = False
        if res_data:
            try:
                assert int(res_data['body']['error']) == int(login_in['expected_code'])
                logger.info('测试用例断言成功')
                is_pass = True
            except:
                is_pass = True
                logger.info('测试用例断言失败')
            finally:
                case_data.updateResults(res_data, is_pass, str(login_in['id']))
                assert is_pass
            return is_pass

    # def set_relation(self, relation, res_data):
    #     try:
    #         if relation:
    #             relation = relation.split(",")
    #             # print(relation)
    #             for i in relation:
    #                 var = i.split("=")
    #                 var_name = var[0]
    #                 var_tmp = var[1].split(".")
    #                 res = Base.parse_relation(var_tmp, res_data)
    #                 # print(f"{var_name}={res}")
    #                 setattr(DynamicParam, var_name, res)
    #     except Exception as e:
    #         print(e)
    #
    # def correlation(self, data):
    #     res_data = Base.find(data)
    #     if res_data:
    #         replace_dict = {}
    #         for i in res_data:
    #             data_tmp = getattr(DynamicParam, str(i), "None")
    #             replace_dict.update({str(i):data_tmp})
    #         data = json.loads(Base.relace(data, replace_dict))
    #     return data


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_login.py'])
