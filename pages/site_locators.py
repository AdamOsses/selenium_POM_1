from selenium.webdriver.common.by import By


class SiteLocators:
    # Whole site locators
    PRODUCTS_STORE = (By.ID, "nava")
    HOME = (By.XPATH, '//a[@class="navbar-brand"]')
    CONTACT = (By.XPATH, '//*[@data-target="#exampleModal"]')
    ABOUT_US = (By.XPATH, '//*[@data-target="#videoModal"]')
    CART = (By.ID, "cartur")
    LOG_IN = (By.ID, "login2")
    SIGN_UP = (By.ID, "signin2")
    LOG_OUT = (By.ID, "logout2")
    WELCOME_USER = (By.ID, "nameofuser")

    PAGE_URL = {
        "home_page": "https://www.demoblaze.com/index.html",
        "product_page": "https://www.demoblaze.com/prod.html?idp_=",
        "cart_page": "https://www.demoblaze.com/cart.html"
    }

# login: ahk
# password: ahk
