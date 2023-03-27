from selenium.webdriver.common.by import By
from pages.site_locators import SiteLocators


class ProductPageLocators(SiteLocators):
    PRODUCT_IMAGE = (By.XPATH, '//div[@class="item active"]/img')
    PRODUCT_NAME = (By.XPATH, '//h2[@class="name"]')
    PRODUCT_PRICE = (By.XPATH, '//h3[@class="price-container"]')
    PRODUCT_DESCRIPTION = (By.ID, 'more-information')

    ADD_TO_CART_BUTTON = ((By.XPATH, '//a[@class="btn btn-success btn-lg"]'))
