#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/28
import requests


class Base:

    def __init__(self, corpsecret):
        self.host = 'https://qyapi.weixin.qq.com'
        self.corpsecret = corpsecret
        self.session = requests.session()
        accesstoken = self._get_accesstoken()
        self.session.params = {'access_token': accesstoken}

    def _get_accesstoken(self):
        params = {'corpid': 'ww242cd7f7c0d1e378',
                  'corpsecret': self.corpsecret}
        res = self.send('GET', self.host+'/cgi-bin/gettoken', params)
        return res.json()['access_token']

    def send(self, method, url, *args, **kwargs):
        if not url.startswith('http'):
            url = '/'.join((self.host, url))
        return self.session.request(method, url, *args, **kwargs)



