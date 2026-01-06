from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time


def  test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()

    # Добавим ожидание появления алерта
    time.sleep(2)

    product_page.solve_quiz_and_get_code()
    #time.sleep(1000)
    product_page.should_be_message_about_adding_product_name()
    product_page.should_be_message_about_adding_product_cost()