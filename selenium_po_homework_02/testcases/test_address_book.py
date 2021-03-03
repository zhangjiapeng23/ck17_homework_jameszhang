#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/3
import time

import pytest

from page.main_page import MainPage


class TestAddressBook:

    def setup_method(self):
        self.main_page = MainPage()
        print('Test start.')

    def teardown_method(self):
        self.main_page.quit()
        print('Test end.')

    @pytest.mark.parametrize('username, alias, telephone, address, title',
                             [('zhangjiapeng', '12', '99993', 'changsha', 'tester'),
                              ('jameszhang', 'jameszhang', '', '', 'developer'),
                              ('sky', 'zhang', '0', '111111', 'mamager')])
    def test_add_member(self, username, alias, telephone, address, title):
        accid = int(time.time())
        email = str(accid) + '@163.com'
        self.main_page.switch_to_address().enter_add_member_page().add_member(username=username,
                                                                              alias=alias,
                                                                              acctid=accid,
                                                                              telephone=telephone,
                                                                              email=email,
                                                                              address=address,
                                                                              title=title)
        time.sleep(4)


