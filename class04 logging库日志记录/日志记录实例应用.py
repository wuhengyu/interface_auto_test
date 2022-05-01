# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 15:16
# @Author  : Walter
# @File    : 日志记录实例应用.py
# @License : (C)Copyright Walter
# @Desc    :
import logging

logger = logging.getLogger('测试日志输出:')
logger.setLevel(logging.DEBUG)

# 创建文件输出对象fh
fh = logging.FileHandler('日志记录实例应用.log', mode='a', encoding='utf-8')
# 设置级别
fh.setLevel(logging.DEBUG)
# 设置格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# 添加logger对象
logger.addHandler(fh)

try:
    open('/not/exit/file', 'rb')
    logger.info('true')
except:
    logger.error('error')