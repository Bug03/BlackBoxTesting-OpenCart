import time

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from utils.conftest import Driver


class TestLogin(Driver):
    def test_login(self, driver):
        login_page = LoginPage(driver)
        # Go to login page
        login_page.go_to_login_page()
        # Login
        login_page.login('nchd03112003@gmail.com', '1234')
        # index.php?route=account/account
        assert "account/account" in login_page.get_current_url()

    # no have account and password
    def test_login_with_no_email_and_password(self, driver):
        login_page = LoginPage(driver)
        # Go to login page
        login_page.go_to_login_page()
        # Login
        login_page.login('', '')
        # error message is displayed
        notification = login_page.get_error_message()
        # Warning: No match for E-Mail Address and/or Password.
        assert "Warning: No match for E-Mail Address and/or Password." in notification

    # without exists account in database
    def test_login_with_not_exists_account(self, driver):
        login_page = LoginPage(driver)
        # Go to login page
        login_page.go_to_login_page()
        # Login
        login_page.login('demo111111111@gmail.com', '1234')
        # error message is displayed
        notification = login_page.get_error_message()
        # Warning: No match for E-Mail Address and/or Password.
        assert "Warning: No match for E-Mail Address and/or Password." in notification

    # with invalid creditials
    def test_login_with_invalid_creditials(self, driver):
        login_page = LoginPage(driver)
        # Go to login page
        login_page.go_to_login_page()
        # Login
        login_page.login('@#@#@gmail.com', '@#@#')
        # error message is displayed
        notification = login_page.get_error_message()

        # Warning: No match for E-Mail Address and/or Password.
        assert "Warning: No match for E-Mail Address and/or Password." in notification

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        # Go to login page
        login_page.go_to_login_page()
        # Login
        login_page.login('nchd03112003@gmail.com', '1234')
        # logout
        login_page.logout()
        # index.php?route=account/logout
        assert "account/logout" in login_page.get_current_url()













