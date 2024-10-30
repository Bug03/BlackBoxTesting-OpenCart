from utils.conftest import Driver
from pages.add_to_cart import AddToCart
from pages.search import Search
import pytest
import random

class TestAddToCart(Driver):
    available_products = [
        {'name': 'MacBook', 'unit_price': '$602.00'},
        {'name': 'iPhone', 'unit_price': '$123.20'},
        {'name': 'HTC Touch HD', 'unit_price': '$122.00'},
        {'name': 'Palm Treo Pro', 'unit_price': '$337.99'},
        {'name': 'iPod Classic', 'unit_price': '$122.00'},
    ]

    @pytest.mark.parametrize("testcase, expected_total_price", [
        (

                {
                    'name': 'MacBook',
                    'unit_price': '$602.00',
                    'quantity': str(random.randint(1, 5))  # Random quantity between 1 and 5
                },

                lambda testcase: float(testcase['unit_price'].replace('$', '')) * int(testcase['quantity'])
        ),
        (
                {
                    'name': 'iPhone',
                    'unit_price': '$123.20',
                    'quantity': str(random.randint(1, 5))  # Random quantity between 1 and 5
                },

                lambda testcase: float(testcase['unit_price'].replace('$', '')) * int(testcase['quantity'])

        )
    ])
    def test_add_single_product_to_cart(self, driver, testcase, expected_total_price):
        """
        Test add single product to cart
        Args:
            driver: webdriver
            testcase: dict with keys: name, unit_price, quantity
            expected_total_price: float
        """
        add_to_cart = AddToCart(driver)

        expected_product_details_list = [{
            'name': testcase['name'],
            'unit_price': testcase['unit_price'],
            'quantity': testcase['quantity']
        }]

        search = Search(driver)
        search.go_to_home_page()
        search.search(testcase['name'])
        search.scroll_to_first_product()
        add_to_cart.choose_product_by_name(testcase['name'])
        add_to_cart.add_to_cart_in_product_page_with_qty(testcase['quantity'])
        add_to_cart.scroll_to_top()
        add_to_cart.go_to_cart_page()
        actual_product_details = add_to_cart.get_product_info_in_cart()
        actual_total_price = add_to_cart.get_total_price()
        print("Actual product details:", actual_product_details)
        print("Actual total price:", actual_total_price)

        assert actual_product_details == expected_product_details_list
        assert actual_total_price == expected_total_price(testcase)

    @pytest.mark.parametrize("testcases, expected_total_price", [
        (
                random.sample(available_products, 2),  # Randomly select 2 products
                lambda testcases: sum(
                    float(product['unit_price'].replace('$', '')) * int(product['quantity']) for product in testcases)
        ),
        (
                random.sample(available_products, 3),  # Randomly select 3 products
                lambda testcases: sum(
                    float(product['unit_price'].replace('$', '')) * int(product['quantity']) for product in testcases)
        )
    ])
    def test_add_multi_product_to_cart(self, driver, testcases, expected_total_price):
        """
        Test add multiple products to cart
        Args:
            driver: webdriver
            testcases: list of dicts with keys: name, unit_price, quantity
            expected_total_price: float
        """
        add_to_cart = AddToCart(driver)
        search = Search(driver)
        expected_product_details_list = []

        for testcase in testcases:
            testcase['quantity'] = str(random.randint(1, 5))  # Random quantity between 1 and 5
            expected_product_details_list.append({
                'name': testcase['name'],
                'unit_price': testcase['unit_price'],
                'quantity': testcase['quantity']
            })

            search.go_to_home_page()
            search.search(testcase['name'])
            search.scroll_to_first_product()
            add_to_cart.choose_product_by_name(testcase['name'])
            add_to_cart.add_to_cart_in_product_page_with_qty(testcase['quantity'])
            add_to_cart.scroll_to_top()

        add_to_cart.go_to_cart_page()
        actual_product_details = add_to_cart.get_product_info_in_cart()
        actual_total_price = add_to_cart.get_total_price()
        print("Actual product details:", actual_product_details)
        print("Actual total price:", actual_total_price)

        # Sort the lists before asserting
        expected_product_details_list = sorted(expected_product_details_list, key=lambda x: x['name'])
        actual_product_details = sorted(actual_product_details, key=lambda x: x['name'])

        assert actual_product_details == expected_product_details_list
        assert actual_total_price == expected_total_price(testcases)

    def test_add_to_cart_with_invalid_qty(self, driver):
        """
        Test add to cart with invalid quantity
        Notes:
        - Expected: Error message
        - Actual: Success message
        """
        add_to_cart = AddToCart(driver)
        search = Search(driver)
        search.go_to_home_page()
        search.search('MacBook')
        search.scroll_to_first_product()
        add_to_cart.choose_product_by_name('MacBook')
        add_to_cart.add_to_cart_in_product_page_with_qty('abc')
        # print message add to cart
        print(add_to_cart.get_message())
        expectedMessage = "Error: You must enter a valid quantity"
        assert add_to_cart.get_message() == expectedMessage

    def test_add_to_cart_with_empty_qty(self, driver):
        """
        Test add to cart with empty quantity
        Notes:
        - Expected: Error message
        - Actual: Success message
        """
        add_to_cart = AddToCart(driver)
        search = Search(driver)
        search.go_to_home_page()
        search.search('MacBook')
        search.scroll_to_first_product()
        add_to_cart.choose_product_by_name('MacBook')
        add_to_cart.add_to_cart_in_product_page_with_qty('')
        # print message add to cart
        print(add_to_cart.get_message())
        expectedMessage = "Error: You must enter a valid quantity"
        assert add_to_cart.get_message() == expectedMessage

    def test_add_to_cart_with_zero_qty(self, driver):
        """
        Test add to cart with zero quantity
        Notes:
        - Expected: Error message
        - Actual: Error message
        """
        add_to_cart = AddToCart(driver)
        search = Search(driver)
        search.go_to_home_page()
        search.search('MacBook')
        search.scroll_to_first_product()
        add_to_cart.choose_product_by_name('MacBook')
        add_to_cart.add_to_cart_in_product_page_with_qty('0')
        # print message add to cart
        print(add_to_cart.get_message())
        expectedMessage = "Error: You must enter a valid quantity"
        assert add_to_cart.get_message() == expectedMessage