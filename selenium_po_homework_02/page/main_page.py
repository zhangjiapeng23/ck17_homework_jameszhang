#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/3

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

from page.address_book_page import AddressBookPage


class MainPage:

    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def switch_to_address(self):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()
        return AddressBookPage(self.driver)

    def quit(self):
        self.driver.quit()
