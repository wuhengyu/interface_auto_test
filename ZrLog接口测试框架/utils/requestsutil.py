# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 15:29
# @Author  : Walter
# @File    : requestsutil.py
# @License : (C)Copyright Walter
# @Desc    :
import json

import requests

from ZrLog接口测试框架.utils.logutil import logger
from ZrLog接口测试框架.utils.readmysql import RdTestcase


class RequestSend:

    def api_run(self, url, method, data=None, headers=None, cookies=None):
        res = None
        logger.info('请求的url为{}，类型为{}'.format(url, type(url)))
        logger.info('method为{}，类型为{}'.format(method, type(method)))
        logger.info('请求的data为{}，类型为{}'.format(data, type(data)))
        logger.info('请求的headers为{}，类型为{}'.format(headers, type(headers)))
        logger.info('请求的cookies为{}，类型为{}'.format(cookies, type(cookies)))

        session = requests.session()
        if method == 'get':
            res = session.get(url, params=data, headers=headers, cookies=cookies)
            # logger.info(res.url)
        elif method == 'post':
            if headers == {"Content-Type": "application/json"}:
                res = session.post(url, json=data, headers=headers, cookies=cookies)
                # logger.info(res.url)
            elif headers == {"Content-Type": "application/x-www-form-urlencoded"}:
                res = session.post(url, params=data, headers=headers, cookies=cookies)
        self.dict1 = dict()
        try:
            body = res.json()
        except:
            body = res.text
        self.dict1['body'] = body
        self.cookies = res.cookies
        if self.cookies:
            self.dict1['admin_token'] = self.cookies.values()
            RdTestcase().updateCookies(self.cookies.keys(), self.cookies.values())
        return self.dict1

    def send(self, url, method, **kwargs):
        return self.api_run(url=url, method=method, **kwargs)

