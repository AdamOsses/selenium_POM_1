from selenium.webdriver.common.by import By


class SiteLocators:
    # Whole site locators
    PRODUCTS_STORE = (By.ID, "nava")
    HOME = (By.XPATH, '//a[@class="navbar-brand"]')
