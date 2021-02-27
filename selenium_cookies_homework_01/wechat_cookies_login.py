#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/2/25
import datetime
import json
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWeChat:

    def setup_method(self):
        print("Test start.")
        # self.driver = webdriver.Chrome()

        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(chrome_options=chrome_arg)

        self.driver.implicitly_wait(5)

    def teardown_method(self):
        print("Test end.")
        self.driver.quit()

    def test_login_tm(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')
        element_locator = (By.XPATH, '//*[@class="ww_operationBar"]//*[@class="qui_btn ww_btn js_add_member"]')
        element = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(element_locator))

        # mouse
        # webdriver.ActionChains(self.driver).move_to_element(element).click(element).perform()

        # js
        # self.driver.execute_script("arguments[0].click();", element)

        # origin
        element.click()
        sleep(3)

    def test_save_cookies(self):
        date = datetime.datetime.now().strftime("%Y%m%d")
        cookies_file = os.path.join(os.path.dirname(__file__), 'cookies', date + '_cookies.json')
        if not os.path.exists(cookies_file):
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            cookies = self.driver.get_cookies()
            with open(cookies_file, 'w', encoding='utf-8') as fp:
                json.dump(cookies, fp)

    def test_cookies_login(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        date = datetime.datetime.now().strftime("%Y%m%d")
        cookies_file = os.path.join(os.path.dirname(__file__), 'cookies', date + '_cookies.json')
        with open(cookies_file, 'r', encoding='utf-8') as fp:
            cookies = json.load(fp)

        for i in cookies:
            self.driver.add_cookie(i)

        self.driver.refresh()
        sleep(5)





