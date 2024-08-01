from selenium import webdriver
from fixture.session import SessionHelper
class Application:


    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)


    def submit_the_form(self):
        # submit the form
        wd = self.wd
        wd.find_element_by_id("submit").click()

    def set_address(self, location):
        # set address
        wd = self.wd
        wd.find_element_by_id("currentAddress").send_keys(location.address)
        wd.find_element_by_id("permanentAddress").click()
        wd.find_element_by_id("permanentAddress").clear()
        wd.find_element_by_id("permanentAddress").send_keys(location.address_str)

    def set_email(self, email):
        # set email
        wd = self.wd
        wd.find_element_by_id("userEmail").send_keys(email)
        wd.find_element_by_id("currentAddress").click()
        wd.find_element_by_id("currentAddress").clear()

    def set_username(self, username):
        # set username
        wd = self.wd
        wd.find_element_by_id("userName").send_keys(username)
        wd.find_element_by_id("userEmail").click()
        wd.find_element_by_id("userEmail").clear()

    def choose_item(self):
        # choose item
        wd = self.wd
        wd.find_element_by_id("item-0").click()
        wd.find_element_by_id("userName-label").click()
        wd.find_element_by_id("userName").click()
        wd.find_element_by_id("userName").clear()


    def destroy(self):
        self.wd.quit()


