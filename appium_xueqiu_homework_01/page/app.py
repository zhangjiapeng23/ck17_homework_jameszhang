#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13

from appium.webdriver import Remote

from appium_xueqiu_homework_01.page.base_page import BasePage
from appium_xueqiu_homework_01.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver is None:
            caps = dict()
            caps['platform'] = 'Android'
            caps['appPackage'] = 'com.xueqiu.android'
            caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
            caps['deviceName'] = 'my phone'
            caps['noReset'] = 'true'
            self.driver = Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=caps)
            self.driver.implicitly_wait(8)
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

