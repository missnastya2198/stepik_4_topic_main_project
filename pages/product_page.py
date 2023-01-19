from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла

class ProductPage(BasePage): 
    def add_to_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET) 
        add_basket.click() #click by basket button to open basket
        
    #check that the added book = book page
    def item_is_added(self):
        item_name_1 = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        added_item_name_1 = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME)
        assert item_name_1.text == added_item_name_1.text, "Check the added item in the basket" 
        
    #check that added book price = price in the basket
    def added_item_basket_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)      
        assert item_price.text == basket_price.text, "Check item and basket prices"

    #check that success message should not be presented in the product page       
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    #check that success message should not be presented in 4 sec in the product page 
    def should_not_be_success_message_2(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented in 4 sec, but it should disappear in 4 sec"

    

   

    
