# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 21:56
# @Author  : CC
# @Desc    : test.py
import sys

from py_log import get_logger

if __name__ == '__main__':
    logger = get_logger(__name__)
    logger.info('123456')
    # default_log_path = sys.path[1] + '/logs'
    # print(default_log_path)
