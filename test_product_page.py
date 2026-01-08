import time
import pytest
import random
import string
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.add_product_to_basket
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        test_email = str(time.time()) + "@fakemail.org"
        test_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(9))
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(test_email, test_password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()
        #product_page.go_to_login_page()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()

        # Добавим ожидание появления алерта
        time.sleep(2)

        product_page.solve_quiz_and_get_code()
        #time.sleep(1000)
        product_page.should_be_message_about_adding_product_name()
        product_page.should_be_message_about_adding_product_cost()



def  test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()

    # Добавим ожидание появления алерта
    time.sleep(2)

    product_page.solve_quiz_and_get_code()
    time.sleep(1000)
    product_page.should_be_message_about_adding_product_name()
    product_page.should_be_message_about_adding_product_cost()

@pytest.mark.xfail(reason="need for education")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()

    # Добавим ожидание появления алерта
    time.sleep(2)

    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail(reason="need for education")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()

    # Добавим ожидание появления алерта
    time.sleep(2)

    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_not_be_basket_contains_products()
    basket_page.should_be_basket_is_empty()







