#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
from appium_xueqiu_homework_01.page.base_page import BasePage

from appium.webdriver.common.mobileby import MobileBy


class SearchPage(BasePage):

    def search_keyword(self, keyword):
        self.input_field.send_keys(keyword)
        return self

    @property
    def input_field(self):
        return self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]')
