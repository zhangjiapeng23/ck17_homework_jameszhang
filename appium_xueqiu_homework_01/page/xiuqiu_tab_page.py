#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_homework_01.page.base_page import BasePage


class XiuqiuTabPage(BasePage):

    def enter_edit(self):
        self.pencil_button.click()
        return self

    @property
    def pencil_button(self):
        return self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
