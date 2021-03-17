#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/13
import os


import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es

from appium_xueqiu_homework_02.utils.blacklist_handler import blacklist_handler
from appium_xueqiu_homework_02.utils.logger import log


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @blacklist_handler
    def find(self, *element_selector):
        log.info(f'Find element {element_selector[1]}')
        return WebDriverWait(self.driver, 10).until(es.presence_of_element_located(element_selector))

    def finds(self, *element_selector):
        log.info(f'Find element {element_selector[1]}')
        return self.driver.find_elements(*element_selector)

    def find_and_click(self, *element_selector):
        self.find(*element_selector).click()

    def find_and_send(self, locator, element, val):
        self.find(locator, element).send_keys(val)

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

    def screenshot(self):
        log.info('Get screenshot.')
        return self.driver.get_screenshot_as_png()

    def parse(self, yaml_file, action_name):
        yaml_path = os.path.join(os.path.dirname(__file__), '..', 'page', 'yaml', yaml_file)
        with open(yaml_path, 'r') as fp:
            page = yaml.safe_load(fp)

        steps = page.get(action_name)
        for step in steps:
            action = step.get('action')
            if action == 'find':
                return self.find(step.get('locator'), step.get('value'))
            elif action == 'find_and_click':
                return self.find_and_click(step.get('locator'), step.get('value'))
            elif action == 'find_and_send':
                return self.find_and_send(step.get('locator'), step.get('value'), step.get('content'))
            else:
                log.error(f"Can't parse this action name: {action}")
                return ValueError












