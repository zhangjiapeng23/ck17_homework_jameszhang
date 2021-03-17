#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_homework_02.utils.base_page import BasePage
from appium_xueqiu_homework_02.page.xiuqiu_tab_page import XueqiuTabPage
from appium_xueqiu_homework_02.page.trading_tab_page import TradingTabPage
from appium_xueqiu_homework_02.page.market_tab_page import MarketTabPage


class MainPage(BasePage):

    def _parse(self, action_name,):
        return self.parse('main_page.yml', action_name)

    def enter_xueqiu_tab(self):
        self._parse('enter_xueqiu_tab')
        return XueqiuTabPage(self.driver)

    def enter_trading_tab(self):
        self._parse('enter_trading_tab')
        return TradingTabPage(self.driver)

    def enter_market_tab(self):
        self._parse('enter_market_tab')
        return MarketTabPage(self.driver)

