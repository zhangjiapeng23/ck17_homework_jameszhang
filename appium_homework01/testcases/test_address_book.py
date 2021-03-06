#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/6
import random

import pytest

from appium_homework01.page.main_page import MainPage


class TestAddressBook:

    def setup_method(self):
        print('test start.')

    def teardown_metos(self):
        print('test end.')

    @pytest.mark.parametrize('name', [('james',), ('zhangzhang',)])
    def test_add_member(self, name):
        phone = random.randint(13300000000, 13399999999)
        main_page = MainPage()
        main_page.enter_address_book().\
            enter_add_member_page().\
            enter_manually_add_page().\
            add_a_member(name, phone)
