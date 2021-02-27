#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @time  : 2021/1/29 1:22 上午

import pytest
import yaml
import allure

from python_project.calculator import Calculator


@allure.feature("Get two numbers sum.")
@pytest.mark.add
class TestCalculatorAdd:

    @allure.story("Get two int numbers sum.")
    def test_add_int(self, new_calculator, prepare_calculate, get_add_int_data):
        a, b, res = get_add_int_data
        cal = new_calculator
        with allure.step('step 1: sum the two numbers.'):
            res_ = cal.add(a, b)

        with allure.step('step 2: check the result'):
            assert res_ == res

    @allure.story("Get two float numbers sum.")
    def test_add_float(self, new_calculator, prepare_calculate, get_add_float_data):
        a, b, res = get_add_float_data
        with allure.step('step 1: sum the two numbers.'):
            res_ = new_calculator.add(a, b)

        with allure.step('step 2: check the result'):
            assert round(res_, 3) == round(res, 3)


@allure.feature("divide two numbers.")
@pytest.mark.div
class TestCalculatorDiv:

    @allure.story("divide two int numbers.")
    def test_div_int(self, new_calculator, prepare_calculate, get_div_int_data):
        a, b, res = get_div_int_data
        with allure.step('step 1: divide two numbers.'):
            res_ = new_calculator.div(a, b)

        with allure.step('step 2: check the result'):
            assert round(res_, 2) == round(res, 2)

    @allure.story("divide two float numbers.")
    # @pytest.mark.run(order=2)
    def test_div_float(self, new_calculator, prepare_calculate, get_div_float_data):
        a, b, res = get_div_float_data
        with allure.step('step 1: divide two numbers.'):
            res_ = new_calculator.div(a, b)

        with allure.step('step 2: check the result'):
            assert round(res_, 2) == round(res, 2)

    @allure.story("when divisor is zero")
    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.run(order=-1)
    def test_div_zero_divisor(self, new_calculator, prepare_calculate, get_div_divisor_zero_data):
        a, b, res = get_div_divisor_zero_data
        with allure.step('step 1: divide two numbers.'):
            try:
                res_ = new_calculator.div(a, b)
            except ZeroDivisionError:
                res_ = 'error'

        with allure.step('step 2: check the result'):
            assert res_ == res

        with pytest.raises(ZeroDivisionError):
            new_calculator.div(a, b)


@pytest.mark.mul
class TestCalculatorMul:
    # todo: add mul function testcases
    pass


@pytest.mark.sub
class TestCalculatorSub:
    # todo: add sub function testcases
    pass








