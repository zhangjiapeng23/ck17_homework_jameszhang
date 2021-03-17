#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/15
from functools import wraps

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import allure

from appium_xueqiu_homework_02.utils.logger import log

BLACK_LIST = ('//*[@text="test_not_find"]',
              '//*[@resource-id="com.xueqiu.android:id/iv_close"]',
              '//*[@resource-id="com.xueqiu.android:id/image_cancel"]')


def blacklist_handler(func):

    @wraps(func)
    def wrap(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except (NoSuchElementException, TimeoutException) as exc:
            for black in BLACK_LIST:
                self.driver.implicitly_wait(1)
                element = self.finds(MobileBy.XPATH, black)
                self.driver.implicitly_wait(6)
                if element:
                    element[0].click()

                    # use handle_blacklist decorator call func again,
                    # to deal with multiple blacklist display at same time.
                    decorator = blacklist_handler(func)
                    return decorator(self, *args, *kwargs)
            else:
                allure.attach(self.screenshot(), attachment_type=allure.attachment_type.PNG)
                log.error(f'Element find failed: {exc}')
                raise exc

    return wrap



