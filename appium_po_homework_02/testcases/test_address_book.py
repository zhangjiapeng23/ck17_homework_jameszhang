#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/6
import random
from time import sleep

import pytest

from appium_po_homework_02.page.app import APP


class TestAddressBook:

    @classmethod
    def setup_class(cls):
        print('init driver')
        cls.app = APP()

    @classmethod
    def teardown_class(cls):
        print('quit driver')
        cls.app.quit()

    def setup_method(self):
        print('test start.')
        self.app.launch()

    def teardown_metos(self):
        print('test end.')
        self.app.close()

    @pytest.mark.parametrize('name', [('james',), ('zhang',)])
    def test_add_member(self, name):
        phone = random.randint(13300000000, 13399999999)
        main_page = self.app.enter_main_page()
        main_page.enter_address_book().\
            enter_add_member_page().\
            enter_manually_add_page().\
            add_a_member(name, phone)

        # check add success toast
        main_page.get_toast_add_member_success()

    @pytest.mark.parametrize('name', [('james',), ('zhang',)])
    def test_remove_member_from_search(self, name):
        main_page = self.app.enter_main_page()
        search_page = main_page.enter_address_book().\
            enter_search_page().search_key_world(name)
        result_total = len(search_page.get_search_result_list())

        search_page.click_first_item().show_more_function().\
            enter_edit_member_page().remove_member()

        # wait result refresh
        sleep(4)
        removed_result_total = len(search_page.get_search_result_list())

        assert result_total == removed_result_total + 1

