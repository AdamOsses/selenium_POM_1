from selenium.webdriver.common.by import By
from pages.site_locators import SiteLocators


class HomePageLocators(SiteLocators):
    PRODUCTS = (By.XPATH, '//img[@class="card-img-top img-fluid"]')
