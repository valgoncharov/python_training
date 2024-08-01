class GroupHelper:

    def __init__(self, app):
        self.app = app

    def set_address(self, location):
        # set address
        wd = self.app.wd
        wd.find_element_by_id("currentAddress").send_keys(location.address)
        wd.find_element_by_id("permanentAddress").click()
        wd.find_element_by_id("permanentAddress").clear()
        wd.find_element_by_id("permanentAddress").send_keys(location.address_str)

    def set_email(self, email):
        # set email
        wd = self.app.wd
        wd.find_element_by_id("userEmail").send_keys(email)
        wd.find_element_by_id("currentAddress").click()
        wd.find_element_by_id("currentAddress").clear()

    def set_username(self, username):
        # set username
        wd = self.app.wd
        wd.find_element_by_id("userName").send_keys(username)
        wd.find_element_by_id("userEmail").click()
        wd.find_element_by_id("userEmail").clear()