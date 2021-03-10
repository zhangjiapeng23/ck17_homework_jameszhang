#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/9
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from appium_po_homework_02.log import logger


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, element_selector):
        try:
            logger.debug('find element %s', element_selector[1])
            return self.driver.find_element(*element_selector)
        except Exception as exc:
            logger.error(exc)

    def finds(self, element_selector):
        try:
            logger.debug('find elements %s', element_selector[1])
            return self.driver.find_elements(*element_selector)
        except Exception as exc:
            logger.error(exc)

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
                logger.info('scroll up page')
                max_time -= 1
        logger.error('scroll up page to max times, not find element %s', element_selector[1])
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
                logger.info('scroll down page')
                max_time -= 1
        logger.error('scroll down page to max times, not find element %s', element_selector[1])
        raise NoSuchElementException(element_selector)

    def get_toast_add_member_success(self):
        logger.info("find '添加成功' toast")
        return self.find((MobileBy.XPATH, '//*[@text="添加成功"]'))
