from selenium.webdriver.common.by import By

class MainPageLocators():

    LOGIN_LINK = (By.ID, "registration_link")

class LoginPageLocators():

    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():

    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success:first-child .alertinner strong")
    TOTAL_PRICE_AFTER_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
