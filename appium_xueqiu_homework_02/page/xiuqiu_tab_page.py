#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu_homework_02.utils.base_page import BasePage


class XueqiuTabPage(BasePage):

    def _parse(self, action_name):
        return self.parse('xueqiu_tab_page.yml', action_name)

    def enter_edit(self):
        self._parse('enter_edit')
        return self

