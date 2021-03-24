#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/24
import json
import os

from mitmproxy import http


# --ssl-insecure

class LocalRewrite:

    def __init__(self):
        self.local_file = os.path.join(os.path.dirname(__file__), 'quote.json')

    def request(self, flow: http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json" in flow.request.pretty_url:
            with open(self.local_file) as f:
                flow.response = http.HTTPResponse.make(status_code=200,
                                                       content=f.read(),
                                                       headers={"Content-Type": "application/json;charset=UTF-8"})


class Rewrite:

    def handle_data(self, data):
        if isinstance(data, dict):
            for k, v in data.items():
                data[k] = self.handle_data(v)

        elif isinstance(data, list):
            data = [self.handle_data(i) for i in data]

        elif isinstance(data, int):
            if data > 0:
                data = -20
            else:
                data = 100

        elif isinstance(data, float):
            data = -data

        elif isinstance(data, str):
            if data == '腾讯控股':
                data = 'JamesZhang 控股'
        else:
            data = data

        return data

    def response(self, flow: http.HTTPFlow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json" in flow.request.pretty_url:
            data = self.handle_data(json.loads(flow.response.text))
            flow.response.text = json.dumps(data)


class Test:

    def __init__(self):
        self.local_file = os.path.join(os.path.dirname(__file__), 'quote.json')

    def request(self, flow: http.HTTPFlow):
        if 'https://www.baidu.com' in flow.request.pretty_url:
            with open(self.local_file) as f:
                flow.response = http.HTTPResponse.make(status_code=200,
                                                       content=f.read(),
                                                       headers={"Content-Type": "text/html"})


addons = [
    Test(), Rewrite(), LocalRewrite()
]



