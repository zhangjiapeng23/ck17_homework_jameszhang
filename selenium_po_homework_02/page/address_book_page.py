#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/3
import random

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressBookPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_add_member_page(self):
        self.__add_member_button_header().click()
        return self

    def add_member(self, **test_data):
        self.__name_input_field().send_keys(test_data['username'])
        self.__alias_input_field().send_keys(test_data['alias'])
        self.__acctid_input_field().send_keys(test_data['acctid'])
        self.__telephone_input_field().send_keys(test_data['telephone'])
        self.__email_input_field().send_keys(test_data['email'])
        self.__address_input_field().send_keys(test_data['address'])
        self.__title_input_field().send_keys(test_data['title'])
        self.__save_buttons()[random.randint(0, 1)].click()
        return self

    def __add_member_button_header(self):
        element_locator = (By.XPATH, '//*[@class="ww_operationBar"]//*[@class="qui_btn ww_btn js_add_member"]')
        add_member_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element_locator))
        return add_member_button

    def __add_member_button_footer(self):
        add_member_button = self.driver.find_element(By.XPATH, '//*[@class="js_operationBar_footer ww_operationBar"]//'
                                                               '*[@class="qui_btn ww_btn js_add_member"]')
        return add_member_button

    def __name_input_field(self):
        input_field = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        return input_field

    def __alias_input_field(self):
        input_field = self.driver.find_element(By.XPATH, '//*[@id="memberAdd_english_name"]')
        return input_field

    def __acctid_input_field(self):
        input_field = self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]')
        return input_field

    def __telephone_input_field(self):
        input_field = self.driver.find_element(By.XPATH, '//*[@id="memberAdd_telephone"]')
        return input_field

    def __email_input_field(self):
        input_field = self.driver.find_element(By.XPATH, '//*[@id="memberAdd_mail"]')
        return input_field

    def __address_input_field(self):
        input_field = self.driver.find_element(By.XPATH, '//*[@id="memberEdit_address"]')
        return input_field

    def __title_input_field(self):
        input_field = self.driver.find_element(By.XPATH, '//*[@id="memberAdd_title"]')
        return input_field

    def __save_buttons(self):
        save_buttons = self.driver.find_elements(By.XPATH, '//*[@class="member_colRight_operationBar ww_operationBar"]'
                                                           '//*[@class="qui_btn ww_btn js_btn_save"]')
        return save_buttons


