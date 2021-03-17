#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
from appium_xueqiu_homework_02.utils.base_page import BasePage


class SearchPage(BasePage):

    def _parse(self, action_name):
        return self.parse('search_page.yml', action_name)

    def search_keyword(self, keyword):
        self._parse('search_keyword').send_keys(keyword)
        return self
