from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_IN_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_IN_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_CONFIRM_IN_REGISTER_FORM =(By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")



class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    NAME_PRODUCT_WHEN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    COST_PRODUCT_WHEN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alertinner > p > strong")
    NAME_PRODUCT_IN_PAGE = (By.XPATH, "//div[@class='row']//h1")
    COST_PRODUCT_IN_PAGE = (By.XPATH, "//div[@class='row']//p[@class='price_color']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'] [1]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SEE_BASKET_LINK = (By.XPATH, "//a[text()='Посмотреть корзину']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']//p")
    BASKET_CONTAINS_PRODUCTS =(By.CSS_SELECTOR, "#basket_formset")




