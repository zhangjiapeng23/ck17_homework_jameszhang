#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/9
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, element_selector):
        return self.driver.find_element(*element_selector)

    def finds(self, element_selector):
        return self.driver.find_elements(*element_selector)

    def scroll_up_find(self, element_selector, max_time=5):
        while max_time:
            self.driver.implicitly_wait(1)
            element = self.finds(element_selector)
            self.driver.implicitly_wait(5)
            if element:
                return element[0]
            else:
                screen_size = self.driver.get_window_size()
                width = screen_size['width']
                height = screen_size['height']
                self.driver.swipe(width*0.5, height*0.75, width*0.5, height*0.25)
                max_time -= 1
        raise NoSuchElementException(element_selector)

    def scroll_down_find(self, element_selector, max_time=5):
        while max_time:
            self.driver.implicitly_wait(1)
            element = self.finds(element_selector)
            self.driver.implicitly_wait(5)
            if element:
                return element[0]
            else:
                screen_size = self.driver.get_window_size()
                width = screen_size['width']
                height = screen_size['height']
                self.driver.swipe(width*0.5, height*0.25, width*0.5, height*0.75)
                max_time -= 1
        raise NoSuchElementException(element_selector)

    def get_toast_add_member_success(self):
        return self.find((MobileBy.XPATH, '//*[@text="添加成功"]'))
