# -*- coding: utf-8 -*-
# @Time    : 2022/5/2 23:05
# @Author  : Walter
# @File    : logutil.py
# @License : (C)Copyright Walter
# @Desc    :
import os.path

from ZrLog接口测试框架.config import setting
import logging
import time

STREAM = True


class LogUtil:
    def __init__(self):
        self.logger = logging.getLogger("自动化测试")
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            # self.log_name = '{}.log'.format(time.strftime("%Y_%m_%d %H:%M:%S", time.localtime()))
            self.log_name = '{}.log'.format(time.strftime("%Y_%m_%d", time.localtime()))
            self.log_path_file = os.path.join(setting.get_log_path(), self.log_name)
        fh = logging.FileHandler(self.log_path_file, encoding='utf-8', mode='a')
        fh.setLevel(logging.DEBUG)
        # 设置打印格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # 添加handler
        self.logger.addHandler(fh)
        fh.close()
        if STREAM:
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(logging.DEBUG)
            fh_stream.setFormatter(formatter)
            self.logger.addHandler(fh_stream)

    def log(self):
        return self.logger


logger = LogUtil().log()

if __name__ == '__main__':
    logger.debug('-----调试信息[debug]-----')
    logger.info('-----调试信息[info]-----')
    logger.warning('-----调试信息[warning]-----')
    logger.error('-----调试信息[error]-----')
    logger.critical('-----调试信息[critical]-----')
