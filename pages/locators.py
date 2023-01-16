from selenium.webdriver.common.by import By


class MainPageLocators():
    
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    #ITEM_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main > :nth-child(1)")
    ADDED_ITEM_NAME = (By.XPATH, "//div[@id='messages']/div[1]/div[1]/strong")

    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main > :nth-child(2)")
    BASKET_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div[1]/p[1]/strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    

