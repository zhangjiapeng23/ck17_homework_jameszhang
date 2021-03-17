#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/15
import datetime
import os
import subprocess
import signal
from time import sleep

import pytest
import allure

from utils.logger import init_logger, log
from appium_xueqiu_homework_02.page.app import App


@pytest.fixture(scope='session', autouse=True)
def init_app():
    app = App()
    log.info('Completed init app test config.')
    yield app
    app.quit()
    log.info('Quit app test.')


@pytest.fixture(scope='session', autouse=True)
def init_log():
    init_logger()
    log.info('Completed init logger config.')


@pytest.fixture(scope='function', autouse=False)
def record():
    ctime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    record_video = os.path.join(os.path.dirname(__file__), '..', 'report', 'videos', f'{ctime}.mp4')
    cmd = f'scrcpy -Nr {record_video}'
    log.info('Start record video.')
    p = subprocess.Popen(cmd, shell=True, encoding='utf-8')
    yield
    os.kill(p.pid, signal.SIGINT)
    log.info('Video record completed.')

    # pause 2 seconds wait video push completed.
    sleep(2)
    with open(record_video, 'rb') as fp:
        allure.attach(fp.read(), name='test_record', attachment_type=allure.attachment_type.MP4)


@pytest.fixture(scope='function', autouse=True)
def case_setup(init_app):
    log.info('Test case start.')
    app = init_app
    app.start()
    yield app.enter_main_page()
    log.info('Test case end.')





