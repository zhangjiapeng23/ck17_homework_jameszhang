#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/9

from appium.webdriver.common.mobileby import MobileBy

from appium_po_homework_02.page.base_page import BasePage
from appium_po_homework_02.page.address_book_page import AddressBookPage


class MainPage(BasePage):

    def enter_address_book(self):
        self.__address_book().click()
        return AddressBookPage(self.driver)

    def __address_book(self):
        return self.find((MobileBy.XPATH, '//*[@text="通讯录"]'))



