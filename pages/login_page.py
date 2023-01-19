from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException # в начале файла


class LoginPage(BasePage):
    #execution 3 methods by should_be_login_page()
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "login is absent in current url"
        #check that url is correct

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form link is not presented"
        # check that login form is presented 
        

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form link is not presented"
        # check that registration form is presented

    #refistration a new user in the login page
    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        input3.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()

   

        