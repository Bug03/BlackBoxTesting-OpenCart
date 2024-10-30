import time

from unicodedata import category

from utils.conftest import Driver
from pages import Search

class TestSearch(Driver):
    def test_search(self, driver):
        """
        Test search with keyword Macbook
        Notes:
        - Expected: MacBook, MacBook Air, MacBook Pro
        - Actual: MacBook, MacBook Air, MacBook Pro
        """
        search_page = Search(driver)
        # Search in home page
        search_page.go_to_home_page()
        # Search
        search_page.search('Macbook')
        # Get search results
        product_result = search_page.get_search_details_results()
        expected_data = ['MacBook', 'MacBook Air', 'MacBook Pro']

        # print product result
        print ([product['name'] for product in product_result])
        # assert ['MacBook', 'MacBook Air', 'MacBook Pro'] in product_result
        assert any(data in [product['name'] for product in product_result] for data in expected_data)

        time.sleep(2)

    def test_search_description(self, driver):
        """
        Test search with option search in product description

        Notes:
        - Expected: keyword ( Macbook ) in description for each product
         with category Laptops & Notebooks
        - Actual: Actual result is the same as expected
        """
        search_page = Search(driver)
        # Go to search page
        search_page.go_to_search_page()
        keyword = "Macbook"
        categories = "Laptops & Notebooks"
        # Search with option search in product description
        search_page.search_description(keyword, categories)
        time.sleep(2)
        # Get search results
        product_result = search_page.get_search_details_results()

        # assert keywork in description for each product
        for product in product_result:
            assert keyword.lower() in product['description'].lower()

    def test_search_invalid_keyword(self, driver):
        """
        Test search with invalid keyword
        Notes:
        - Exepected: No product found
        - Actual: No product found
        """
        search_page = Search(driver)
        # Go to search page
        search_page.go_to_search_page()
        # Search with invalid keyword
        search_page.search('####')
        time.sleep(2)
        # Get search results
        product_result = search_page.get_search_details_results()
        # assert no product found
        assert len(product_result) == 0

    def test_search_with_percent(self, driver):
        """
        Test search with percent
        Notes:
        - Exepected: No product found
        - But the actual result is: all products are found
        """

        search_page = Search(driver)
        # Go to search page
        search_page.go_to_search_page()
        # Search with invalid keyword
        search_page.search('%')
        time.sleep(2)
        # Get search results
        product_result = search_page.get_search_name_of_results()
        # assert no product found and print the error message
        assert len(product_result) == 0

    def test_search_in_search_page(self, driver):
        search_page = Search(driver)
        # Go to search page
        search_page.go_to_search_page()
        # Search
        search_page.search_in_search_page('Macbook', 'Laptops & Notebooks')
        time.sleep(2)
        # Get search results
        product_result = search_page.get_search_details_results()
        expected_data = ['MacBook', 'MacBook Air', 'MacBook Pro']

        # print expected_data
        print("Expected data: ", expected_data)

        # print actual product result
        print("Actual product result: ", [product['name'] for product in product_result])
        # assert ['MacBook', 'MacBook Air', 'MacBook Pro'] in product_result
        assert any(data in [product['name'] for product in product_result] for data in expected_data)

        time.sleep(2)

    def test_search_empty_keyword(self, driver):
        search_page = Search(driver)
        # Go to search page
        search_page.go_to_search_page()
        # Search
        search_page.search('')
        time.sleep(2)
        # Get search results
        product_result = search_page.get_search_details_results()
        # assert no product found
        assert len(product_result) == 0