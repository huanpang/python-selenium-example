from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.ID, 'header-login-link')

class LoginPageLocators(object):
    USERNAME = (By.ID, 'login-username')
    PWD = (By.ID, 'login-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'form button')