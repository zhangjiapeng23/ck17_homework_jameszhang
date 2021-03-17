#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13

from appium_xueqiu_homework_02.utils.base_page import BasePage
from appium_xueqiu_homework_02.page.search_page import SearchPage


class MarketTabPage(BasePage):

    def _parse(self, action_name):
        return self.parse('market_tab_page.yml', action_name)

    def enter_search_page(self):
        self._parse('enter_search_page')
        return SearchPage(self.driver)

