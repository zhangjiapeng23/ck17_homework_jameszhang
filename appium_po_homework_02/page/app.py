#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/6
import time

from appium import webdriver

from appium_po_homework_02.page.base_page import BasePage
from appium_po_homework_02.page.main_page import MainPage


class APP(BasePage):

    def launch(self):
        if self.driver is None:
            caps = dict()
            caps['platform'] = 'Android'
            caps['deviceName'] = 'Android Phone'
            caps['appPackage'] = 'com.tencent.wework'
            caps['appActivity'] = 'com.tencent.wework.launch.LaunchSplashActivity'
            caps['noReset'] = 'true'
            caps['settings[waitForIdleTimeout]'] = 1
            caps['unicodeKeyboard'] = 'true'
            caps['resetKeyboard'] = 'true'
            self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_capabilities=caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def enter_main_page(self):
        return MainPage(self.driver)







