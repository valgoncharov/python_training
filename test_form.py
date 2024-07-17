# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestForm(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path=r'')
        self.wd.implicitly_wait(30)
    
    def test_form(self):
        wd = self.wd
        wd.get("https://demoqa.com/forms")
        wd.find_element_by_xpath("//div[@id='app']/div/div/div/div/div/div/div/span/div").click()
        wd.get("https://demoqa.com/text-box")
        wd.find_element_by_id("item-0").click()
        wd.find_element_by_id("userName-label").click()
        wd.find_element_by_id("userName").click()
        wd.find_element_by_id("userName").clear()
        wd.find_element_by_id("userName").send_keys("Ujy")
        wd.find_element_by_id("userEmail").click()
        wd.find_element_by_id("userEmail").clear()
        wd.find_element_by_id("userEmail").send_keys("val@gmail.com")
        wd.find_element_by_id("currentAddress").click()
        wd.find_element_by_id("currentAddress").clear()
        wd.find_element_by_id("currentAddress").send_keys("fsaa")
        wd.find_element_by_id("permanentAddress").click()
        wd.find_element_by_id("permanentAddress").clear()
        wd.find_element_by_id("permanentAddress").send_keys("acsd")
        wd.find_element_by_id("submit").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
