#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
import random

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


def handle_blacklist(func):
    black_list = ['//*[@text="test_not_find"]',
                  '//*[@resource-id="com.xueqiu.android:id/iv_close"]',
                  '//*[@resource-id="com.xueqiu.android:id/image_cancel"]']

    def warp(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except NoSuchElementException as exc:
            for black in black_list:
                self.driver.implicitly_wait(1)
                element = self.finds(MobileBy.XPATH, black)
                self.driver.implicitly_wait(6)
                if element:
                    element[0].click()

                    # use handle_blacklist decorator call func again,
                    # to deal with multiple blacklist display at same time.
                    decorator = handle_blacklist(func)
                    return decorator(self, *args, *kwargs)
            else:
                raise exc
    return warp


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_blacklist
    def find(self, *element_selector):
        return self.driver.find_element(*element_selector)

    def finds(self, *element_selector):
        return self.driver.find_elements(*element_selector)

    def scroll_up_find(self, *element_selector, max_time=5):
        while max_time:
            self.driver.implicitly_wait(2)
            element = self.finds(element_selector)
            self.driver.implicitly_wait(5)
            if element:
                return element[0]
            else:
                screen_size = self.driver.get_window_size()
                width = screen_size['width']
                height = screen_size['height']
                self.driver.swipe(width * 0.5, height * 0.75, width * 0.5, height * 0.25)
                max_time -= 1
        raise NoSuchElementException(element_selector)






