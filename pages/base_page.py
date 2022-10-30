from pages.site_locators import SiteLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_page_url(self, name):
        return SiteLocators.PAGE_URL[name]

    # entire site buttons
    def home_button_click(self):
        pass

    def contact_button_click(self):
        pass

    def about_us_button_click(self):
        pass

    def cart_button_click(self):
        pass

    def log_in_button_click(self):
        pass

    def sign_up_button_click(self):
        pass

    def log_out_button_click(self):
        pass






