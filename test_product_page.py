import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time
import faker

#need_review tests for 4_3final step. Execution command: pytest -s -m need_review --tb=line C:\Users\aniv0121\stepik_4_topic_main_project\test_product_page.py

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        #generation email and password for every next test
        f = faker.Faker()
        email = f.email()
        password = "black1234512399211wfeewf"
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password) #register a user
        register_user = BasePage(browser, link)
        register_user.should_be_authorized_user() #check that user is registered
        #print("user is registered")

    #check that logged in user can add a book to the basket 
    def test_user_can_add_product_to_basket(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()    
        calculate = BasePage(browser, link)
        calculate.solve_quiz_and_get_code()
        page.item_is_added()
        page.added_item_basket_price()

@pytest.mark.need_review
#check that guest (NOT logged in user) can add a book to the basket 
def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    calculate = BasePage(browser, link)
    calculate.solve_quiz_and_get_code()
    page.item_is_added()
    page.added_item_basket_price()

@pytest.mark.need_review
#check that guest (NOT logged in user) see an empty basket after leaving a product page
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, link)
    basket_page.basket_should_be_empty()

@pytest.mark.need_review
#check that guest (NOT logged in user) can go to login page from a product page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
        

#xfail for failed tests (they will not be fixed in the future)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    calculate = BasePage(browser, link)
    calculate.solve_quiz_and_get_code()
    page.should_not_be_success_message()

#guest doesn't see the success message about adding a book to the basket
def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

#xfail for failed tests (they will not be fixed in the future)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    calculate = BasePage(browser, link)
    calculate.solve_quiz_and_get_code()
    page.should_not_be_success_message_2()

#login link is presented for guest
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
        




