import pytest
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import time
#pytest -rsx --tb=line --language=en C:\Users\aniv0121\stepik_4_topic_main_project\test_product_page.py
#link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"

'''@pytest.mark.parametrize('num', [pytest.param("offer7", marks=pytest.mark.xfail(reason = "some bug")),'offer0', 'offer1', 'offer2', 'offer3', 'offer4', 'offer5', 'offer6',  'offer8', 'offer9'])
          
#@pytest.mark.parametrize('num', [pytest.param("offer7", marks=pytest.mark.xfail(reason = "some bug")),'offer0'])
def test_guest_can_add_product_to_basket(browser, num):
    link = f"https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo={num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
   
    calculate = BasePage(browser, link)
    calculate.solve_quiz_and_get_code()
    page.item_is_added()
    page.added_item_basket_price()
    #time.sleep(90)'''


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    calculate = BasePage(browser, link)
    calculate.solve_quiz_and_get_code()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    calculate = BasePage(browser, link)
    calculate.solve_quiz_and_get_code()
    page.should_not_be_success_message_2()

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
    page.go_to_login_page()


