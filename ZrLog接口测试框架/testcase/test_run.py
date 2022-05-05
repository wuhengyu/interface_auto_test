# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 19:24
# @Author  : Walter
# @File    : test_run.py
# @License : (C)Copyright Walter
# @Desc    :
import datetime
from ZrLog接口测试框架.config.setting import DynamicParam
from ZrLog接口测试框架.utils.logutil import logger
import ZrLog接口测试框架.common.base as Base
import json
import pytest
from ZrLog接口测试框架.utils.requestsutil import RequestSend
from ZrLog接口测试框架.utils.readmysql import RdTestcase

attribute = DynamicParam()
case_data = RdTestcase()
case_list = case_data.is_run_data('zrlog', '登录模块')
case_list2 = case_data.is_run_data('zrlog', '登录模块')[5]
print(case_list2)
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class TestApi:
    def setup_class(self):
        logger.info(f"开始执行用例，开始时间为{current_time}")

    def teardown_class(self):
        logger.info(f"执行用例完成，结束时间为{current_time}")

    @pytest.mark.parametrize('case', [case_list2])
    def test_run(self, case):
        res_data = None

        url = case_data.loadConfKey('zrlog', 'url_api')['value'] + case['url']
        # url = None
        # for _ in case_list2:
        #     url = case_data.loadConfKey('zrlog', 'url_api')['value']
        #     api_url = _['url']
        #     url = url + api_url
        # url = url[0]

        method = case['method']
        headers = eval(case['headers'])
        cookies = eval(case['cookies'])
        data = eval(case['request_body'])
        relation = str(case['relation'])
        case_name = case['title']
        headers = self.correlation(headers)
        cookies = self.correlation(cookies)
        data = self.correlation(data)
        try:
            logger.info('正在执行{}用例'.format(case_name))
            res_data = RequestSend().send(url, method, data=data, headers=headers, cookies=cookies)
            logger.info("用例执行成功，请求结果为{}".format(res_data))
        except:
            logger.info("用例执行失败，请查看日志查找原因")
            assert False
        if res_data:
            if relation != "None":
                self.set_relation(relation, res_data)
        self.assert_respoes(case, res_data)
        return res_data

    def assert_respoes(self, case, res_data):
        is_pass = False
        try:
            assert int(res_data['body']['error']) == int(case['expected_code'])
            logger.info('用例断言成功')
            is_pass = True
        except:
            is_pass = False
            logger.info('用例断言失败')
        finally:
            case_data.updateResults(res_data, is_pass, str(case['id']))
            assert is_pass
        return is_pass

    def set_relation(self, relation, res_data):
        try:
            if relation:
                relation = relation.split(",")
                for i in relation:
                    var = i.split("=")
                    var_name = var[0]
                    var_tmp = var[1].split(".")
                    res = Base.parse_relation(var_tmp, res_data)
                    print(f"{var_name}={res}")
                    setattr(DynamicParam, var_name, res)
        except Exception as e:
            print(e)

    def correlation(self, data):
        res_data = Base.find(data)
        if res_data:
            replace_dict = {}
            for i in res_data:
                data_tmp = getattr(DynamicParam, str(i), "None")
                replace_dict.update({str(i):data_tmp})
            data = json.loads(Base.relace(data, replace_dict))
        return data

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_run.py'])