from selenium.webdriver.common.by import By
from pages.site_locators import SiteLocators


class HomePageLocators(SiteLocators):
    PRODUCTS = (By.XPATH, '//img[@class="card-img-top img-fluid"]')
    PRODUCT_NAME = []
    PRODUCT_PRICE = []
    PRODUCT_DESCRIPTION = []
    # max 9 products on page
    for i in range(1, 10):
        PRODUCT_NAME.append((By.XPATH, f'(//a[@class="hrefch"])[{i}]'))
        PRODUCT_PRICE.append((By.XPATH, f'(//div[@class="card h-100"]//h5)[{i}]'))
        PRODUCT_DESCRIPTION.append((By.XPATH, f'(//div[@class="card h-100"]//p)[{i}]'))
    NEXT_BUTTON = (By.ID, 'next2')
    PREVIOUS_BUTTON = (By.ID, 'prev2')
