#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/9

from appium.webdriver.common.mobileby import MobileBy

from appium_po_homework_02.page.base_page import BasePage


class SearchPage(BasePage):

    def search_key_world(self, key_word):
        self.__search_input_box().send_keys(key_word)
        return self

    def get_search_result_list(self):
        return self.__search_result_list()

    def click_first_item(self):
        self.get_search_result_list()[0].click()
        return PersonalInfoPage(self.driver)

    def __search_input_box(self):
        search_input_box = self.find((MobileBy.XPATH, '//*[@text="搜索"]'))
        return search_input_box

    def __search_result_list(self):
        search_result_list = self.finds((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dil"]'))
        return search_result_list


class PersonalInfoPage(BasePage):

    def show_more_function(self):
        self.__unfold_page_icon().click()
        return self

    def enter_edit_member_page(self):
        self.__edit_member().click()
        return PersonalInfoEditPage(self.driver)

    def __unfold_page_icon(self):
        return self.find((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/iga"]'))

    def __edit_member(self):
        return self.find((MobileBy.XPATH, '//*[@text="编辑成员"]'))


class PersonalInfoEditPage(BasePage):

    def remove_member(self):
        self.__remove_member_button().click()
        self.__confirm().click()
        return SearchPage(self.driver)

    def __confirm(self):
        return self.find((MobileBy.XPATH, '//*[@text="确定"]'))

    def __remove_member_button(self):
        return self.scroll_up_find((MobileBy.XPATH, '//*[@text="删除成员"]'))
