#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/6

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from appium_homework01.page.address_book_page import AddressBookPage


class MainPage:

    def __init__(self):
        caps = dict()
        caps['platform'] = 'Android'
        caps['deviceName'] = 'Android Phone'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = 'com.tencent.wework.launch.LaunchSplashActivity'
        caps['noReset'] = 'true'
        caps['settings[waitForIdleTimeout]'] = 1
        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_capabilities=caps)
        self.driver.implicitly_wait(5)

    def enter_address_book(self):
        self.__address_book().click()
        return AddressBookPage(self.driver)

    def quit(self):
        self.driver.quit()

    def __address_book(self):
        address_book = self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]')
        return address_book





