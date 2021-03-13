#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_homework_01.page.base_page import BasePage
from appium_xueqiu_homework_01.page.search_page import SearchPage


class MarketTabPage(BasePage):

    def enter_search_page(self):
        self.search_icon.click()
        return SearchPage(self.driver)

    @property
    def search_icon(self):
        return self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
