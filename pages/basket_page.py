from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text, "Basket is not empty"

    def should_not_be_basket_contains_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTAINS_PRODUCTS), "Basket contains products"
