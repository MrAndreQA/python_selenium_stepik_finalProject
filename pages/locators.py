from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    NAME_PRODUCT_WHEN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    COST_PRODUCT_WHEN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner > p > strong")
    NAME_PRODUCT_IN_PAGE = (By.XPATH, "//div[@class='row']//h1")
    COST_PRODUCT_IN_PAGE = (By.XPATH, "//div[@class='row']//p[@class='price_color']")


