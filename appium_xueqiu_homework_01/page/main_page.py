#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_homework_01.page.base_page import BasePage
from appium_xueqiu_homework_01.page.xiuqiu_tab_page import XiuqiuTabPage
from appium_xueqiu_homework_01.page.trading_tab_page import TradingTabPage
from appium_xueqiu_homework_01.page.market_tab_page import MarketTabPage


class MainPage(BasePage):

    def enter_xueqiu_tab(self):
        self.xiuqiu_bottom_tab.click()
        return XiuqiuTabPage(self.driver)

    def enter_trading_tab(self):
        self.trading_bottom_tab.click()
        return TradingTabPage(self.driver)

    def enter_market_tab(self):
        self.market_bottom_tab.click()
        return MarketTabPage(self.driver)

    @property
    def xiuqiu_bottom_tab(self):
        return self.find(MobileBy.XPATH, '//*[@text="雪球"]')

    @property
    def trading_bottom_tab(self):
        return self.find(MobileBy.XPATH, '//*[@text="交易"]')

    @property
    def market_bottom_tab(self):
        return self.find(MobileBy.XPATH, '//*[@text="行情"]')
