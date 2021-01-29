#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @time  : 2021/1/29 1:22 上午

import pytest
import yaml
import allure

from python_project.Calculator import Calculator


@allure.feature("Get two numbers sum.")
@pytest.mark.add
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

    @allure.story("Get two int numbers sum.")
    @pytest.mark.parametrize(('a', 'b', 'res'), data_yaml('int'), ids=ids_yaml('int'))
    def test_add_int(self, a, b, res):
        with allure.step('step 1: sum the two numbers.'):
            res_ = self.cal.add(a, b)

        with allure.step('step 2: check the result'):
            assert res_ == res

    @allure.story("Get two float numbers sum.")
    @pytest.mark.parametrize(('a', 'b', 'res'), data_yaml('float'), ids=ids_yaml('float'))
    def test_add_float(self, a, b, res):
        with allure.step('step 1: sum the two numbers.'):
            res_ = self.cal.add(a, b)

        with allure.step('step 2: check the result'):
            assert round(res_, 3) == round(res, 3)


@allure.feature("divide two numbers.")
@pytest.mark.div
class TestCalculatorDiv:

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

        return data['div'][genre]['data']

    def ids_yaml(genre):
        with open('data/calculator_test_data.yml') as f:
            data = yaml.safe_load(f)

        return data['div'][genre]['ids']

    @allure.story("divide two int numbers.")
    @pytest.mark.parametrize(('a', 'b', 'res'), data_yaml('int'), ids=ids_yaml('int'))
    def test_div_int(self, a, b, res):
        with allure.step('step 1: divide two numbers.'):
            res_ = self.cal.div(a, b)

        with allure.step('step 2: check the result'):
            assert round(res_, 2) == round(res, 2)

    @allure.story("divide two float numbers.")
    @pytest.mark.parametrize(('a', 'b', 'res'), data_yaml('float'), ids=ids_yaml('float'))
    def test_div_float(self, a, b, res):
        with allure.step('step 1: divide two numbers.'):
            res_ = self.cal.div(a, b)

        with allure.step('step 2: check the result'):
            assert round(res_, 2) == round(res, 2)

    @allure.story("when divisor is zero")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(('a', 'b', 'res'), data_yaml('divisor_zero'), ids=ids_yaml('divisor_zero'))
    def test_div_zero_divisor(self, a, b, res):
        with allure.step('step 1: divide two numbers.'):
            try:
                res_ = self.cal.div(a, b)
            except ZeroDivisionError:
                res_ = 'error'

        with allure.step('step 2: check the result'):
            assert res_ == res


@pytest.mark.mul
class TestCalculatorMul:
    # todo: add mul function testcases
    pass


@pytest.mark.sub
class TestCalculatorSub:
    # todo: add sub function testcases
    pass








