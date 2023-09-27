import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class MySeleniumTests(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Edge('msedgedriver.exe')  # Use the appropriate webdriver here
        self.driver.implicitly_wait(10)  # Adjust the wait time as needed

    def tearDown(self):
        self.driver.quit()

    def test_login_view(self):
        self.driver.get(self.live_server_url + '/login/')  # Replace with the actual URL

        # Find and interact with the login form elements
        username_input = self.driver.find_element_by_name('username')
        password_input = self.driver.find_element_by_name('password')
        login_button = self.driver.find_element_by_id('login-button')

        username_input.send_keys('your_username')  # Replace with a valid username
        password_input.send_keys('your_password')  # Replace with a valid password
        login_button.click()

        # You can now add assertions to check if the login was successful
        self.assertTrue('Blog Application' in self.driver.title)

