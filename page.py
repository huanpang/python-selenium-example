
from locators import MainPageLocators
from locators import LoginPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_url_matches(self):
        return "utm_medium=partner_sms" in self.driver.current_url

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        element.click()


class LoginPage(BasePage):

    def login_free_user(self):
        username = self.driver.find_element(*LoginPageLocators.USERNAME)
        pwd = self.driver.find_element(*LoginPageLocators.PWD)
        submit = self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)

        username.send_keys("huanp_171002_090750")
        pwd.send_keys("test")
        submit.click()

    def is_logged_in(self):
        return "Log in." not in self.driver.page_source