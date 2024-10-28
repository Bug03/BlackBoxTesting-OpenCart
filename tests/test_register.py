import time

from pages.register_page import RegisterPage
from utils.conftest import Driver


class TestRegister(Driver):
    def test_register(self, driver):
        register_page = RegisterPage(driver)
        # Go to register page
        register_page.go_to_register_page()
        # Register
        register_page.register('Danh', 'Nguyen', 'demo1234@gmail.com', '1234')
        # index.php?route=account/account
        time.sleep(2)
        assert "account/success" in register_page.get_current_url()

    # without first name and last name
    def test_register_without_first_name_and_last_name(self, driver):
        register_page = RegisterPage(driver)
        # Go to register page
        register_page.go_to_register_page()
        # Register
        register_page.register('', '', 'demo1234@gmail.com', '1234')
        # error message is displayed
        notification = register_page.get_error_message()

        # First Name must be between 1 and 32 characters!
        # Last Name must be between 1 and 32 characters!
        assert "First Name must be between 1 and 32 characters!" in notification
        assert "Last Name must be between 1 and 32 characters!" in notification
        assert "account/register" in register_page.get_current_url()

    # without email
    def test_register_without_email(self, driver):
        register_page = RegisterPage(driver)
        # Go to register page
        register_page.go_to_register_page()
        # Register
        register_page.register('Danh', 'Nguyen', '', '1234')
        # error message is displayed
        notification = register_page.get_error_message()

        # E-Mail Address does not appear to be valid!
        assert "E-Mail Address does not appear to be valid!" in notification
        assert "account/register" in register_page.get_current_url()

    # without password
    def test_register_without_password(self, driver):
        register_page = RegisterPage(driver)
        # Go to register page
        register_page.go_to_register_page()
        # Register
        register_page.register('Danh', 'Nguyen', '', '')
        # error message is displayed
        notification = register_page.get_error_message()

        # Password must be between 4 and 20 characters!
        assert "Password must be between 4 and 20 characters!" in notification
        assert "account/register" in register_page.get_current_url()

    # without agree
    def test_register_without_agree(self, driver):
        register_page = RegisterPage(driver)
        # Go to register page
        register_page.go_to_register_page()
        # Register
        register_page.register('Danh', 'Nguyen', 'demo1111@gmail.com', '1234', agree=False)
        # error message is displayed
        notification = register_page.get_error_message()

        # Warning: You must agree to the Privacy Policy!
        assert "Warning: You must agree to the Privacy Policy!" in notification
        assert "account/register" in register_page.get_current_url()

    # with exists email
    def test_register_with_exists_email(self, driver):
        register_page = RegisterPage(driver)
        # Go to register page
        register_page.go_to_register_page()
        # Register
        register_page.register('Danh', 'Nguyen', 'nchd03112003@gmail.com', '1234')
        # error message is displayed
        notification = register_page.get_error_message()
        time.sleep(2)

        # Warning: E-Mail Address is already registered!
        assert "Warning: E-Mail Address is already registered!" in notification
        assert "account/register" in register_page.get_current_url()

    # with invalid email

    def test_register_with_invalid_email(self, driver):
        register_page = RegisterPage(driver)
        # Go to register page
        register_page.go_to_register_page()
        # Register
        register_page.register('Danh', 'Nguyen', '@@@gmail.com', '1234')
        # error message is displayed
        notification = register_page.get_error_message()


        # notification có tồn tại lỗi
        print(notification)
        assert notification != []
        assert "account/register" in register_page.get_current_url()

    # with long first name and last name
    def test_register_with_long_first_name_and_last_name(self, driver):
        register_page = RegisterPage(driver)
        # Go to register page
        register_page.go_to_register_page()
        # Register
        register_page.register('Danh' * 10, 'Nguyen' * 10, 'abcde@gmail.com', '1234')
        # error message is displayed
        notification = register_page.get_error_message()

        # First Name must be between 1 and 32 characters!
        # Last Name must be between 1 and 32 characters!
        assert "First Name must be between 1 and 32 characters!" in notification
        assert "Last Name must be between 1 and 32 characters!" in notification
        assert "account/register" in register_page.get_current_url()

    # with short password
    def test_register_with_short_password(self, driver):
        register_page = RegisterPage(driver)
        # Go to register page
        register_page.go_to_register_page()
        # Register
        register_page.register('Danh', 'Nguyen', 'abcde@gmail.com', '123')
        # error message is displayed
        notification = register_page.get_error_message()

        # Password must be between 4 and 20 characters!
        assert "Password must be between 4 and 20 characters!" in notification
        assert "account/register" in register_page.get_current_url()





