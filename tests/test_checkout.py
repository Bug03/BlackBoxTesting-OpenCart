import time
from tabnanny import check

from pages.checkout import Checkout
from pages.add_to_cart import AddToCart
from utils.conftest import Driver
from pages.search import Search

class TestCheckout(Driver):
    def test_checkout_guest(self, driver):
        """
        Test checkout as guest.

        Steps:
        1. Prepare the product before checkout.
        2. Navigate to the checkout page.
        3. Fill in the guest checkout details.
        4. Assert that the order has been placed successfully.

        Args:
            driver: WebDriver instance.
        """
        checkout = Checkout(driver)
        checkout.prepare_product_before_checkout()
        checkout.go_to_checkout()
        checkout.fill_checkout_guest_details(
            first_name='John',
            last_name='Doe',
            email= "nchd03112003@gmail.com",
            company='Test Company',
            address='Test Address',
            city='Test City',
            post_code='12345',
            country='Viet Nam',
            region='Ho Chi Minh City'
        )
        assert checkout.get_message() == 'Your order has been placed!'


    def test_checkout_register(self, driver):
        """
        Test checkout as registered user.

        Steps:
        1. Prepare the product before checkout.
        2. Navigate to the checkout page.
        3. Fill in the registered user checkout details.
        4. Assert that the order has been placed successfully.

        Args:
            driver: WebDriver instance.
        """
        checkout = Checkout(driver)
        checkout.prepare_product_before_checkout()
        checkout.go_to_checkout()
        checkout.fill_checkout_register_details(
            first_name='John',
            last_name='Doe',
            email= "hihihihihi@gmail.com",
            password= '123456',
            company='Test Company',
            address='Test Address',
            city='Test City',
            post_code='12345',
            country='Viet Nam',
            region='Ho Chi Minh City'
        )
        assert checkout.get_message() == 'Your order has been placed!'


    def test_checkout_guest_invalid(self, driver):
        """
        Test checkout as guest with invalid data.

        Steps:
        1. Prepare the product before checkout.
        2. Navigate to the checkout page.
        3. Fill in the guest checkout details with invalid data.
        4. Assert that the appropriate error messages are displayed.

        Args:
            driver: WebDriver instance.
        """
        checkout = Checkout(driver)
        checkout.prepare_product_before_checkout()
        checkout.go_to_checkout()
        checkout.fill_checkout_guest_details(
            # tất cả đều rỗng trừ region và country
            first_name='',
            last_name='',
            email= '',
            company='',
            address='',
            city='',
            post_code='111',
            country='Viet Nam',
            region='Ho Chi Minh City'
        )
        # assert với các error message
        assert checkout.get_error_message('fname_not_exist') == 'First Name must be between 1 and 32 characters!'
        assert checkout.get_error_message('lname_not_exist') == 'Last Name must be between 1 and 32 characters!'
        assert checkout.get_error_message('email_not_exist') == 'E-Mail address does not appear to be valid!'
        assert checkout.get_error_message('address_not_exist') == 'Address 1 must be between 3 and 128 characters!'
        assert checkout.get_error_message('city_not_exist') == 'City must be between 2 and 128 characters!'


    def test_checkout_register_invalid(self, driver):
        """
        Test checkout as registered user with invalid data.

        Steps:
        1. Prepare the product before checkout.
        2. Navigate to the checkout page.
        3. Fill in the registered user checkout details with invalid data.
        4. Assert that the appropriate error messages are displayed.

        Args:
            driver: WebDriver instance.
        """
        checkout = Checkout(driver)
        checkout.prepare_product_before_checkout()
        checkout.go_to_checkout()
        checkout.fill_checkout_register_details(
            # tất cả đều rỗng trừ region và country
            first_name='',
            last_name='',
            email= '',
            password= '',
            company='',
            address='',
            city='',
            post_code='111',
            country='Viet Nam',
            region='Ho Chi Minh City'
        )
        # assert với các error message
        assert checkout.get_error_message('fname_not_exist') == 'First Name must be between 1 and 32 characters!'
        assert checkout.get_error_message('lname_not_exist') == 'Last Name must be between 1 and 32 characters!'
        assert checkout.get_error_message('email_not_exist') == 'E-Mail address does not appear to be valid!'
        assert checkout.get_error_message('address_not_exist') == 'Address 1 must be between 3 and 128 characters!'
        assert checkout.get_error_message('city_not_exist') == 'City must be between 2 and 128 characters!'
        assert checkout.get_error_message('password_not_exist') == 'Password must be between 4 and 20 characters!'




