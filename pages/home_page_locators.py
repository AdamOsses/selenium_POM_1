from selenium.webdriver.common.by import By
from pages.site_locators import SiteLocators


class HomePageLocators(SiteLocators):
    PRODUCTS = (By.XPATH, '//img[@class="card-img-top img-fluid"]')
    PRODUCT_NAME = (By.XPATH, '//a[@class="hrefch"]')
    NEXT_BUTTON = (By.ID, 'next2')
    PREVIOUS_BUTTON = (By.ID, 'prev2')
