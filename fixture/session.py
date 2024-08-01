class SessionHelper:

    def __init__(self, app):
        self.app = app

    def go_to_text_box_page(self, text_box_url):
        # go to text box page
        wd = self.app.wd
        self.app.wd.get(text_box_url)

    def choose_form_page(self):
        # choose form page
        wd = self.app.wd
        self.app.wd.find_element_by_xpath("//div[@id='app']/div/div/div/div/div/div/div/span/div").click()

    def open_home_page(self, base_url):
        # open home page
        wd = self.app.wd
        self.app.wd.get(base_url)