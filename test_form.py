# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from location import Location
import unittest

class TestForm(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
    
    def test_form(self):
        wd = self.wd
        self.open_home_page(wd, base_url="https://demoqa.com/forms")
        self.choose_form_page(wd)
        self.go_to_text_box_page(wd, text_box_url="https://demoqa.com/text-box")
        self.choose_item(wd)
        self.set_username(wd, username="Ujy")
        self.set_email(wd, email="val@gmail.com")
        self.set_address(wd, Location(address="fsaa", address_str="acsd"))
        self.submit_the_form(wd)

    def submit_the_form(self, wd):
        # submit the form
        wd.find_element_by_id("submit").click()

    def set_address(self, wd, location):
        # set address
        wd.find_element_by_id("currentAddress").send_keys(location.address)
        wd.find_element_by_id("permanentAddress").click()
        wd.find_element_by_id("permanentAddress").clear()
        wd.find_element_by_id("permanentAddress").send_keys(location.address_str)

    def set_email(self, wd, email):
        # set email
        wd.find_element_by_id("userEmail").send_keys(email)
        wd.find_element_by_id("currentAddress").click()
        wd.find_element_by_id("currentAddress").clear()

    def set_username(self, wd, username):
        # set username
        wd.find_element_by_id("userName").send_keys(username)
        wd.find_element_by_id("userEmail").click()
        wd.find_element_by_id("userEmail").clear()

    def choose_item(self, wd):
        # choose item
        wd.find_element_by_id("item-0").click()
        wd.find_element_by_id("userName-label").click()
        wd.find_element_by_id("userName").click()
        wd.find_element_by_id("userName").clear()

    def go_to_text_box_page(self, wd, text_box_url):
        # go to text box page
        wd.get(text_box_url)

    def choose_form_page(self, wd):
        # choose form page
        wd.find_element_by_xpath("//div[@id='app']/div/div/div/div/div/div/div/span/div").click()

    def open_home_page(self, wd, base_url):
        # open home page
        wd.get(base_url)

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def test_form_next(self):
        wd = self.wd
        self.open_home_page(wd, base_url="")
        self.choose_form_page(wd)
        self.go_to_text_box_page(wd, text_box_url="")
        self.choose_item(wd)
        self.set_username(wd, username="")
        self.set_email(wd, email="")
        self.set_address(wd, Location(address="", address_str=""))
        self.submit_the_form(wd)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
