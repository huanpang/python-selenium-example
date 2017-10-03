import unittest
from selenium import webdriver
import page

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://testing-url")

    def test_login_in(self):

        main_page = page.MainPage(self.driver)
        assert main_page.is_url_matches(), "UTM tag in url doesn't match."
        main_page.click_go_button()

        login_page = page.LoginPage(self.driver)
        login_page.login_free_user()
        assert login_page.login_free_user(), "Not logged in."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()