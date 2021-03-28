#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/28
from requests_api_homework02.we_work.base import Base


class AddressBook(Base):

    def __init__(self):
        super(AddressBook, self).__init__(corpsecret='611zeR1qXcSektkTj7c7pWzWn1raBrcQpU5szepKZ2E')

    def create_member(self, userid, name, mobile, department, **kwargs):
        path = '/cgi-bin/user/create'
        data = {
            'userid': userid,
            'name': name,
            'mobile': mobile,
            'department': department
        }
        data.update(kwargs)
        res = self.send('POST', path, json=data)
        return res.json()

    def get_member(self, userid):
        path = '/cgi-bin/user/get'
        params = {'userid': userid}
        res = self.send('GET', path, params)
        return res.json()

    def update_member(self, **kwargs):
        path = '/cgi-bin/user/update'
        res = self.send('POST', path, json=kwargs)
        return res.json()

    def delete_member(self, userid):
        path = '/cgi-bin/user/delete'
        params = {'userid': userid}
        res = self.send('GET', path, params)
        return res.json()

