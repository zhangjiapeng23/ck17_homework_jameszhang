#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/6
from appium.webdriver.common.mobileby import MobileBy

from appium_po_homework_02.page.base_page import BasePage
from appium_po_homework_02.page.search_page import SearchPage


class AddressBookPage(BasePage):

    def enter_add_member_page(self):
        self.__add_member_button().click()
        return AddMemberPage(self.driver)

    def enter_search_page(self):
        self.__search_icon().click()
        return SearchPage(self.driver)

    def __add_member_button(self):
        add_member_button = self.scroll_up_find((MobileBy.XPATH, '//*[@text="添加成员"]'))
        return add_member_button

    def __search_icon(self):
        search_icon = self.find((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/igk"]'))
        return search_icon


class AddMemberPage(BasePage):

    def enter_manually_add_page(self):
        self.__manually_add().click()
        return AddMemberFormPage(self.driver)

    def __manually_add(self):
        manually_add = self.find((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
        return manually_add


class AddMemberFormPage(BasePage):

    def add_a_member(self, name, phone):
        self.__name_input_field().send_keys(name)
        self.__phone_input_field().send_keys(phone)
        self.__auto_send_invite_checkbox().click()
        self.__save_button().click()
        return AddMemberPage(self.driver)

    def __name_input_field(self):
        name_input_field = self.find((MobileBy.XPATH, '//*[contains(@text,"姓名")]/../*[@text="必填"]'))
        return name_input_field

    def __phone_input_field(self):
        phone_input_field = self.find((MobileBy.XPATH, '//*[contains(@text,"手机")]/..//*[@text="必填"]'))
        return phone_input_field

    def __auto_send_invite_checkbox(self):
        checkbox = self.find((MobileBy.XPATH, '//*[@text="保存后自动发送邀请通知"]'))
        return checkbox

    def __save_button(self):
        save_button = self.find((MobileBy.XPATH, '//*[@text="保存"]'))
        return save_button
