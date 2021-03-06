#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/6
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class AddressBookPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_add_member_page(self):
        self.__add_member_button().click()
        return AddMemberPage(self.driver)

    def __add_member_button(self):
        add_member_button = self.__scroll_up_find_element((MobileBy.XPATH, '//*[@text="添加成员"]'))
        return add_member_button

    def __scroll_up_find_element(self, element_selector, max_time=3):
        while max_time:
            self.driver.implicitly_wait(1)
            element = self.driver.find_elements(*element_selector)
            self.driver.implicitly_wait(5)
            if element:
                return element[0]
            else:
                screen_size = self.driver.get_window_size()
                width = screen_size['width']
                height = screen_size['height']
                self.driver.swipe(width//2, height//2, width//2, height//2-height//4)
                max_time -= 1
        raise NoSuchElementException(element_selector)


class AddMemberPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_manually_add_page(self):
        self.__manually_add().click()
        return AddMemberFormPage(self.driver)

    def __manually_add(self):
        manually_add = self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]')
        return manually_add


class AddMemberFormPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_a_member(self, name, phone):
        self.__name_input_field().send_keys(name)
        self.__phone_input_field().send_keys(phone)
        self.__auto_send_invite_checkbox().click()
        self.__save_button().click()
        return AddMemberPage(self.driver)

    def __name_input_field(self):
        name_input_field = self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b7m"]')
        return name_input_field

    def __phone_input_field(self):
        phone_input_field = self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/fwi"]')
        return phone_input_field

    def __auto_send_invite_checkbox(self):
        checkbox = self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/fk9"]')
        return checkbox

    def __save_button(self):
        save_button = self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]')
        return save_button
