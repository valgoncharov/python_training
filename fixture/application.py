from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
class Application:


    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def submit_the_form(self):
        # submit the form
        wd = self.wd
        wd.find_element_by_id("submit").click()


    def choose_item(self):
        # choose item
        wd = self.wd
        wd.find_element_by_id("item-0").click()
        wd.find_element_by_id("userName-label").click()
        wd.find_element_by_id("userName").click()
        wd.find_element_by_id("userName").clear()


    def destroy(self):
        self.wd.quit()


