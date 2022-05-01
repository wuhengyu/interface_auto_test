# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 10:15
# @Author  : Walter
# @File    : logging日志级别.py
# @License : (C)Copyright Walter
# @Desc    :

import logging

# 日志级别由低到高
# logging.debug("logging.debug")
# logging.info("logging.info")
# logging.warning("logging.warning")
# logging.error("logging.error")
# logging.critical("logging.critical")


# levelno 日志行号
# message 日志级别名称
# filename 日志信息
# process 进程的ID号
# asctime 日志时间

logging.basicConfig(
    level=logging.INFO,
    # format='%(asctime)s - %(filename)s - [line:%(levelno)d] - %(levelname)s: %(message)s'
    format='%(asctime)s - %(filename)s - 行号:%(lineno)d行 - %(levelname)s: %(message)s'
)


if __name__ == '__main__':
    logging.debug('-----调试信息[debug]-----')
    logging.info('-----调试信息[info]-----')
    logging.warning('-----调试信息[warning]-----')
    logging.error('-----调试信息[error]-----')
    logging.critical('-----调试信息[critical]-----')