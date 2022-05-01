# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 12:11
# @Author  : Walter
# @File    : 输出控制台和文件.py
# @License : (C)Copyright Walter
# @Desc    :
import logging

logger = logging.getLogger('日志输出')
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
fh = logging.FileHandler('输出控制台和文件.log', mode='a', encoding='utf-8')
sh.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
sh.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(sh)
logger.addHandler(fh)


if __name__ == '__main__':
    logger.debug('-----调试信息[debug]-----')
    logger.info('-----调试信息[info]-----')
    logger.warning('-----调试信息[warning]-----')
    logger.error('-----调试信息[error]-----')
    logger.critical('-----调试信息[critical]-----')