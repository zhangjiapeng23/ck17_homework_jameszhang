#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @time  : 2021/1/31 3:56 下午
from typing import List
import random

import pytest
import yaml

from python_project.calculator import Calculator


def data_yaml(func, gener):
    with open('data/calculator_test_data.yml', encoding='utf-8') as f:
        _data = yaml.safe_load(f)
    case = _data[func][gener]
    data = case['data']
    ids = case['ids']
    return data, ids


@pytest.fixture(scope='class')
def new_calculator():
    print("instance a calculator object.")
    cal = Calculator()
    yield cal
    del cal
    print("destroy cal var.")


@pytest.fixture(scope="function")
def prepare_calculate():
    print("【开始计算】")
    yield
    print("【计算结束】")


@pytest.fixture(params=data_yaml('add', 'int')[0], ids=data_yaml('add', 'int')[1])
def get_add_int_data(request):
    return request.param


@pytest.fixture(params=data_yaml('add', 'float')[0], ids=data_yaml('add', 'float')[1])
def get_add_float_data(request):
    return request.param


@pytest.fixture(params=data_yaml('div', 'int')[0], ids=data_yaml('div', 'int')[1])
def get_div_int_data(request):
    return request.param


@pytest.fixture(params=data_yaml('div', 'float')[0], ids=data_yaml('div', 'float')[1])
def get_div_float_data(request):
    return request.param


@pytest.fixture(params=data_yaml('div', 'divisor_zero')[0], ids=data_yaml('div', 'divisor_zero')[1])
def get_div_divisor_zero_data(request):
    return request.param


# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     """Called after collection has been performed. May filter or re-order
#     the items in-place.
#
#     :param pytest.Session session: The pytest session object.
#     :param _pytest.config.Config config: The pytest config object.
#     :param List[pytest.Item] items: List of item objects.
#     """
#     print(items)
#     print(items[2].nodeid)
#     for item in items:
#
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
#
#     random.shuffle(items)