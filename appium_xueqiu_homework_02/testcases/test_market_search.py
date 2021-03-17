#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13

import pytest


class TestMarketSearch:

    def test_handle_blacklist(self, case_setup, record):
        main_page = case_setup
        # trigger login page
        main_page.enter_xueqiu_tab().enter_edit()

        # enter to trading page, auto handle blacklist
        main_page.enter_trading_tab()

    @pytest.mark.parametrize('keyword', [('alibaba',), ('tencent',), ('bilibili', )])
    def test_search_keyword(self, case_setup, keyword):
        main_page = case_setup
        main_page.enter_market_tab().\
            enter_search_page().\
            search_keyword(keyword)


