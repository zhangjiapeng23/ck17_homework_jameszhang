#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @time  : 2021/1/29 1:22 上午

import pytest
import yaml
import allure

from python_project.Calculator import Calculator


class TestCalculatorAdd:

    def setup_class(self):
        self.cal = Calculator()

    def teardown_class(self):
        del self.cal

    def setup(self):
        print("【开始计算】")


    def teardown(self):
        print("【计算结束】")

    def data_yaml(genre):
        with open('data/calculator_test_data.yml') as f:
            data = yaml.safe_load(f)

        return data['add'][genre]['data']

    def ids_yaml(genre):
        with open('data/calculator_test_data.yml') as f:
            data = yaml.safe_load(f)

        return data['add'][genre]['ids']

    @pytest.mark.add
    @pytest.mark.parametrize(('a', 'b', 'res'), data_yaml('int'), ids=ids_yaml('int'))
    def test_add_int(self, a, b, res):
        with allure.step('step 1: sum the two numbers.'):
            sum_ = self.cal.add(a, b)

        with allure.step('step 2: check the result'):
            assert sum_ == res

    @pytest.mark.add
    @pytest.mark.parametrize(('a', 'b', 'res'), data_yaml('float'), ids=ids_yaml('float'))
    def test_add_float(self, a, b, res):
        with allure.step('step 1: sum the two numbers.'):
            sum_ = self.cal.add(a, b)

        with allure.step('step 2: check the result'):
            assert round(sum_, 2) == round(res, 2)







