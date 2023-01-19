from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class BasketPage(BasePage): 
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket should be empty"
        
