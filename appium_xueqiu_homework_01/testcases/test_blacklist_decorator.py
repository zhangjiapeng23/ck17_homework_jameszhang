#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13

import pytest

from appium_xueqiu_homework_01.page.app import App


class TestBlacklistDecorator:

    @classmethod
    def setup_class(cls):
        cls.app = App()

    @classmethod
    def teardown_class(cls):
        cls.app.quit()

    def setup_method(self):
        print('test start')
        self.app.start()

    def teardown_method(self):
        print('test end')

    def test_handle_blacklist(self):
        main_page = self.app.enter_main_page()
        # trigger login page
        main_page.enter_xueqiu_tab().enter_edit()

        # enter to trading page, auto handle blacklist
        main_page.enter_trading_tab()

    @pytest.mark.parametrize('keyword', [('alibaba',), ('tencent',), ('bilibili', )])
    def test_search_keyword(self, keyword):
        main_page = self.app.enter_main_page()
        main_page.enter_market_tab().\
            enter_search_page().\
            search_keyword(keyword)


