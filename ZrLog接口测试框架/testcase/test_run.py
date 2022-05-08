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
case_login_in = case_data.is_run_data('zrlog', '登录模块')[5:6]
case_article = case_data.is_run_data('zrlog', '文章管理模块')[0:1]
case_update = case_data.is_run_data('zrlog', '文章管理模块')[1:2]
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
            data = eval(login_in['request_body'])
            case_name = login_in['title']
            try:
                logger.info('正在执行{}用例'.format(case_name))
                test_login_data = RequestSend().send(url, method, data=data, headers=headers, cookies=cookies)
                logger.info("用例执行成功，请求结果为{}".format(test_login_data))
            except:
                logger.info("用例执行失败，请查看日志查找原因")
                assert False
            self.assert_response(login_in, test_login_data)

    @pytest.mark.parametrize('case_article', [case_article])
    def test_create(self, case_article):
        for article in case_article:
            url = case_data.loadConfKey('zrlog', 'url_api')['value']
            api_url = article['url']
            url = url + api_url
            method = article['method']
            headers = eval(article['headers'])
            data = eval(article['request_body'])
            case_name = article['title']
            cookies = RdTestcase().selectCookies('admin-token')
            try:
                logger.info('正在执行{}用例'.format(case_name))
                self.test_create_data = RequestSend().send(url, method, data=data, headers=headers, cookies=cookies)
                logger.info("用例执行成功，请求结果为{}".format(self.test_create_data))
            except:
                logger.info("用例执行失败，请查看日志查找原因")
                assert False
            finally:
                logId = self.test_create_data['body']['data']['logId']
                alias = self.test_create_data['body']['data']['alias']
                case_data.createID(str(article['id']), logId, alias)

            self.assert_response(article, self.test_create_data)
            return self.test_create_data

    @pytest.mark.parametrize('case_update', [case_update])
    def test_update(self, case_update):
        selectID = case_data.selectID().values()
        selectID = list(selectID)
        logid = alias = selectID[0]
        for article in case_update:
            url = case_data.loadConfKey('zrlog', 'url_api')['value']
            api_url = article['url']
            url = url + api_url
            method = article['method']
            headers = eval(article['headers'])
            data = article['request_body']
            data = eval(data)
            data['logId'] = str(logid)
            data['alias'] = str(alias)
            case_name = article['title']
            cookies = RdTestcase().selectCookies('admin-token')
            try:
                logger.info('正在执行{}用例'.format(case_name))
                test_update_data = RequestSend().send(url, method, data=data, headers=headers, cookies=cookies)
                logger.info("用例执行成功，请求结果为{}".format(test_update_data))
            except:
                logger.info("用例执行失败，请查看日志查找原因")
                assert False
            self.assert_response(article, test_update_data)


    def assert_response(self, expected, res_data):
        is_pass = False
        if res_data:
            try:
                assert int(res_data['body']['error']) == int(expected['expected_code'])
                logger.info('测试用例断言成功')
                is_pass = True
            except:
                is_pass = True
                logger.info('测试用例断言失败')
            finally:
                case_data.updateResults(res_data, is_pass, str(expected['id']))
                assert is_pass
            return is_pass

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_login.py'])
