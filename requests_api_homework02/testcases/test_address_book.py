#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/28
import random

import pytest
from requests_api_homework02.we_work.address_book import AddressBook


class TestAddressBook:
    name = 'jameszhang'
    userid = 'james236'

    def setup_class(self):
        self.request = AddressBook()

    def setup_method(self):
        self.request.delete_member(self.userid)

    def teardown_method(self):
        self.request.delete_member(self.userid)

    def test_get_member(self):
        # create new member
        self.request.create_member(userid=self.userid, name=self.name, mobile='13389888888', department=[1])

        res = self.request.get_member(userid=self.userid)
        assert res['name'] == self.name

    @pytest.mark.parametrize('name', ['test']*10)
    def test_update_member(self, name):
        # create new member
        userid = self.userid + str(random.random())
        mobile = '133999099' + str(random.randint(10, 99))
        self.request.create_member(userid=userid, name=self.name, mobile=mobile, department=[1])

        name = name + str(random.randint(0, 1000))
        res = self.request.update_member(userid=userid, name=name)
        assert res['errmsg'] == 'updated'

        res = self.request.get_member(userid=userid)
        res['name'] = name

        self.request.delete_member(userid=userid)

    def test_create_member(self):
        res = self.request.create_member(userid=self.userid, name=self.name, mobile='13389898888', department=[1])
        assert res['errmsg'] == 'created'

        res = self.request.get_member(userid=self.userid)
        assert res['name'] == self.name

    def test_delete_member(self):
        self.request.create_member(userid=self.userid, name=self.name, mobile='13399888886', department=[1])

        res = self.request.delete_member(self.userid)
        assert res['errmsg'] == 'deleted'

        res = self.request.get_member(self.userid)
        assert res['errcode'] == 60111