from selenium import webdriver
from model.location import Location
class Application:


    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def test_form(self):
        wd = self.wd
        self.open_home_page(base_url="https://demoqa.com/forms")
        self.choose_form_page()
        self.go_to_text_box_page(text_box_url="https://demoqa.com/text-box")
        self.choose_item()
        self.set_username(username="Ujy")
        self.set_email(email="val@gmail.com")
        self.set_address(Location(address="fsaa", address_str="acsd"))
        self.submit_the_form()

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

    def go_to_text_box_page(self, text_box_url):
        # go to text box page
        wd = self.wd
        self.wd.get(text_box_url)

    def choose_form_page(self):
        # choose form page
        wd = self.wd
        self.wd.find_element_by_xpath("//div[@id='app']/div/div/div/div/div/div/div/span/div").click()

    def open_home_page(self, base_url):
        # open home page
        wd = self.wd
        self.wd.get(base_url)

    def destroy(self):
        self.wd.quit()


