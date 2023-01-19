from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest

#need_review tests for 4_3 final step. Execution command: pytest -s  --tb=line C:\Users\aniv0121\stepik_4_topic_main_project\test_main_page.py
#Execution command for mark: pytest -s  -m login_guest --tb=line C:\Users\aniv0121\stepik_4_topic_main_project\test_main_page.py


#check that non-authtorized user can open login page and see login link. Mark login_guest is used for 1 and 2 methods of TestLoginFromMainPage.
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):        
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
#class ends

#check that non-authtorized user can open basket page and see empty basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, link)
    basket_page.basket_should_be_empty()

#check that non-authtorized user can open login page and see login link. Mark login_guest is used for 1 and 2 methods of TestLoginFromMainPage
def test_guest_should_go_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
