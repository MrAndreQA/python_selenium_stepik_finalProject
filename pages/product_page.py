from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_message_about_adding_product_name(self):
        if self.is_element_present(*ProductPageLocators.NAME_PRODUCT_WHEN_ADD_TO_BASKET):
            product_name_expected = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_PAGE).text
            product_name_actual = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_WHEN_ADD_TO_BASKET).text
            assert product_name_expected == product_name_actual, "No product name in the message"
        else:
            raise Exception("No product name")

    def should_be_message_about_adding_product_cost(self):
        if self.is_element_present(*ProductPageLocators.COST_PRODUCT_WHEN_ADD_TO_BASKET):
            product_cost_expected = self.browser.find_element(*ProductPageLocators.COST_PRODUCT_IN_PAGE).text
            product_cost_actual = self.browser.find_element(*ProductPageLocators.COST_PRODUCT_WHEN_ADD_TO_BASKET).text
            assert product_cost_expected == product_cost_actual, "No product cost in the message"
        else:
            raise Exception("No product cost")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"