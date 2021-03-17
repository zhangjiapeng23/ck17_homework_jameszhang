#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
import os

import yaml
from appium.webdriver import Remote

from appium_xueqiu_homework_02.utils.base_page import BasePage
from appium_xueqiu_homework_02.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            app_config = os.path.join(os.path.dirname(__file__), 'yaml', 'app.yml')
            with open(app_config, 'r', encoding='utf-8') as fp:
                app_config = yaml.safe_load(fp)
            desired_caps = app_config.get('desired_capabilities')
            appium_server = app_config.get('appium_server')
            ip = appium_server.get('ip')
            port = appium_server.get('port')
            self.driver = Remote(f'http://{ip}:{port}/wd/hub', desired_capabilities=desired_caps)
            self.driver.implicitly_wait(7)
        else:
            self.driver.launch_app()

    def close(self):
        self.driver.close()

    def restart(self):
        self.close()
        self.start()

    def quit(self):
        self.driver.quit()

    def enter_main_page(self):
        return MainPage(self.driver)

