from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage): 
    def add_to_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET) 
        add_basket.click()
        print("1 is passed")

    def item_is_added(self):
        item_name_1 = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        print("2 is passed")

        added_item_name_1 = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME)
        print("3 is passed")
        #print(item_name_1.text)
        #print(added_item_name_1.text)
        
        assert item_name_1.text == added_item_name_1.text, "Check the added item in the basket"
        print("4 is passed")

    def added_item_basket_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        print("5 is passed")

        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        print("6 is passed")
        #print(item_price.text)
        #print(basket_price.text)
        assert item_price.text == basket_price.text, "Check item and basket prices"
        print("7 is passed")

    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_not_be_success_message_2(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented in 4 sec, but it should disappear in 4 sec"

    

   

    
