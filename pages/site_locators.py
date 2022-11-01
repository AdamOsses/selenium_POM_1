from selenium.webdriver.common.by import By


class SiteLocators:
    # site navbar locators
    PRODUCTS_STORE = (By.ID, "nava")
    HOME = (By.XPATH, '//a[@class="navbar-brand"]')
    CONTACT = (By.XPATH, '//*[@data-target="#exampleModal"]')
    ABOUT_US = (By.XPATH, '//*[@data-target="#videoModal"]')
    CART = (By.ID, "cartur")

    LOG_IN = (By.XPATH, '//a[@style="display: block;" and @id="login2"]') # "display:none" - not visible
    SIGN_UP = (By.XPATH, '//a[@style="display: block;" and @id="signin2"]')
    LOG_OUT = (By.XPATH, '//a[@style="display: block;" and @id="logout2"]')
    WELCOME_USER = (By.XPATH, '//a[@style="display: block;" and @id="nameofuser"]')

    PAGE_URL = {
        "home_page": "https://www.demoblaze.com/index.html",
        "product_page": "https://www.demoblaze.com/prod.html?idp_=",
        "cart_page": "https://www.demoblaze.com/cart.html"
    }

# login: ahk
# password: ahk
