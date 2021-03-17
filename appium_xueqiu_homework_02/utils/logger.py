#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/15
import datetime
import logging
import logging.handlers
import os


def init_logger():
    log = logging.getLogger('Appium')
    formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s'
                                  ' %(module)s.%(funcName)s: %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(logging.INFO)

    date = datetime.date.today().strftime("%Y%m%d")
    log_path = os.path.join(os.path.dirname(__file__), '..', 'report', 'log', f'{date}.log')
    fh = logging.handlers.RotatingFileHandler(filename=log_path, mode='a', encoding='utf-8')
    fh.setFormatter(formatter)
    sh.setLevel(logging.DEBUG)

    log.setLevel(logging.DEBUG)
    log.addHandler(sh)
    log.addHandler(fh)


log = logging.getLogger('Appium')










