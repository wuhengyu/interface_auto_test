# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 11:56
# @Author  : Walter
# @File    : 日志输出文件.py
# @License : (C)Copyright Walter
# @Desc    :

import logging

logger = logging.getLogger('测试日志输出:')
logger.setLevel(logging.DEBUG)

# 创建文件输出对象fh
fh = logging.FileHandler('日志输出文件.log', mode='a', encoding='utf-8')
# 设置级别
fh.setLevel(logging.DEBUG)
# 设置格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# 添加logger对象
logger.addHandler(fh)


if __name__ == '__main__':
    logger.debug('-----调试信息[debug]-----')
    logger.info('-----调试信息[info]-----')
    logger.warning('-----调试信息[warning]-----')
    logger.error('-----调试信息[error]-----')
    logger.critical('-----调试信息[critical]-----')