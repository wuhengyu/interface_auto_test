# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 10:46
# @Author  : Walter
# @File    : 日志输出控制台.py
# @License : (C)Copyright Walter
# @Desc    :
import logging


# 创建logging.getLogger对象
logger = logging.getLogger('logging.getLogger')
# 设置日志输出等级总开关
logger.setLevel(logging.DEBUG)
# 创建控制台实例
sh = logging.StreamHandler()
# 设置控制台输出日志级别
sh.setLevel(logging.DEBUG)
# 设置控制台输出的日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
sh.setFormatter(formatter)
# 加载控制台实例到logger对象中
logger.addHandler(sh)

if __name__ == '__main__':
    logging.debug('-----调试信息[debug]-----')
    logging.info('-----调试信息[info]-----')
    logging.warning('-----调试信息[warning]-----')
    logging.error('-----调试信息[error]-----')
    logging.critical('-----调试信息[critical]-----')