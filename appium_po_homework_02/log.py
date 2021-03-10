#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/10

import logging
import os
import time

logger = logging.getLogger('Appium')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s: %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

log_dir = os.path.join(os.path.dirname(__file__), 'log')
filename = time.strftime('%Y%m%d') + '_log.log'
file_path = os.path.join(log_dir, filename)

fh = logging.FileHandler(filename=file_path, encoding='utf-8')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)

logger.addHandler(fh)
logger.addHandler(ch)


text = "="*20 + time.strftime('%H:%M:%S') + "="*20
logger.info(text)


if __name__ == '__main__':
    logger.debug('debug msg')
    logger.info('info msg')
    logger.warning('warning msg')
    logger.error('error msg')