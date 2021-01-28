#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @time  : 2021/1/28 11:36 下午

class Calculator:

    def __init__(self):
        self.__result = 0

    def add(self, a, b):
        res = a + b
        self.__result = res
        return res

    def sub(self, a, b):
        res = a - b
        self.__result = res
        return res

    def div(self, a, b):
        res = a / b
        self.__result = res
        return res

    def mul(self, a, b):
        res = a * b
        self.__result = res
        return res

    def iadd(self, a):
        self.__result += a
        return self.__result

    def isub(self, a):
        self.__result -= a
        return self.__result

    def imul(self, a):
        self.__result *= a
        return self.__result

    def idiv(self, a):
        self.__result /= a
        return self.__result

    def __repr__(self):
        return str(self.__result)

    @property
    def result(self):
        return self.__result

    def zero(self):
        self.__result = 0

