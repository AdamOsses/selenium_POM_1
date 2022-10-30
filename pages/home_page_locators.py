from selenium.webdriver.common.by import By
from pages.site_locators import SiteLocators


class HomePageLocators(SiteLocators):
    CONTACT_MODAL = (By.XPATH, '//div[@class="modal fade show" and @id="exampleModal"]')
    CONTACT_MODAL_MAIL = (By.ID, 'recipient-email')
    CONTACT_MODAL_NAME = (By.ID, 'recipient-name')
    CONTACT_MODAL_MESSAGE = (By.ID, 'message-text')

    ABOUT_US_MODAL = (By.XPATH, '//div[@class="modal fade show" and @id="videoModal"]')

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
