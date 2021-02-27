#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @time  : 2021/2/6 9:26 下午
import pytest

def check_my_test():
    print("test pytest ini file.")
    pytest.assume(1 == 4)
    pytest.assume(3 > 2)
    pytest.assume(7 >= 9)


