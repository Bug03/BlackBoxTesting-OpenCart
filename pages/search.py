import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Search:
    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get('http://localhost:8080/opencart-site/')
        time.sleep(2)

    def go_to_search_page(self):
        self.driver.get('http://localhost:8080/opencart-site/')
        # click button search in header in order to go to search page
        self.driver.find_element(By.XPATH, '/html/body/header/div/div/div[2]/div/button').click()
        time.sleep(2)

    def search(self, keyword):
        """
        Search bar in home page
        Args:
            keyword: search keyword
        """
        self.driver.find_element(By.NAME, 'search').send_keys(keyword)
        self.driver.find_element(By.XPATH, '//*[@id="search"]/button').click()
        time.sleep(2)

    def search_in_search_page(self, keyword, categories):
        """
        Search in search page
        Args:
            keyword: search keyword
            categories: search category
        Returns: None
        """
        # enter search keyword
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[2]/div[1]/input').send_keys(keyword)
        # select category
        self.select_category(categories)
        # click search button
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[3]/div/button').click()
        time.sleep(2)

    def get_search_name_of_results(self):
        """
        Retrieve search name of results from the current page.
        Returns:
            list: A list of product names.
        """
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, '.product-thumb h4 a')
        return [product.text for product in product_elements]

    def get_search_details_results(self):
        """
        Retrieve search details results from the current page.

        This method navigates through the product elements on the current page,
        collects their details, and returns a list of product information. It
        handles cases where no products are found and ensures that each product
        is processed only once.

        Returns:
            list: A list of dictionaries containing product details.
        """
        product_details = []
        visited_urls = set()

        # Check if there are any products
        if not self.has_products():
            print("No products found.")
            return product_details

        all_products_processed = False
        while not all_products_processed:
            self.scroll_to_first_product()
            product_elements = self.get_product_elements()

            if not product_elements:
                break

            for product in product_elements:
                if self.process_product(product, visited_urls, product_details):
                    break
            else:
                all_products_processed = True

        return product_details

    def has_products(self):
        """
        Check if there are any products on the current page.
        Returns:
            bool: True if products are found, False otherwise.
        """
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, '.product-thumb')
        return bool(product_elements)

    def scroll_to_first_product(self):
        self.scroll_to_element(self.driver.find_element(By.CSS_SELECTOR, '.product-thumb'))

    def get_product_elements(self):
        """
        Retrieve product elements from the current page.
        Returns:
            list: A list of product elements.
        """
        return self.driver.find_elements(By.CSS_SELECTOR, '.product-thumb')

    def process_product(self, product, visited_urls, product_details):
        """
        Process a product element.
        Args:
            product: The product element to process.
            visited_urls: A set of visited product URLs.
            product_details: A list of product details.
        Returns:
            bool: True if the product was processed, False otherwise.
        """
        product_link = product.find_element(By.CSS_SELECTOR, 'h4 a')
        product_url = product_link.get_attribute('href')

        if product_url in visited_urls:
            return False

        visited_urls.add(product_url)
        name = product_link.text
        product_link.click()

        description = self.get_product_description()
        product_details.append({
            'name': name,
            'description': description
        })

        self.driver.back()
        return True

    def get_product_description(self):
        """
        Retrieve the description of a product.
        Returns:
            str: The product description.
        """
        element_description = self.driver.find_element(By.XPATH, '//*[@id="tab-description"]/div')
        if element_description is None:
            element_description = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/p')

        self.scroll_to_element(element_description)
        return element_description.text

    def select_category(self, category):
        # select category by visible text
        select = Select(self.driver.find_element(By.ID, 'input-category'))
        select.select_by_visible_text(category)
        time.sleep(2)

    def search_description(self, keyword, categories):
        """
        Search with option search in product description
        Args:
            keyword: search keyword
            categories: search category
        Returns: None
        """
        # enter search keyword
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[2]/div[1]/input').send_keys(keyword)
        # select category
        self.select_category(categories)
        # check input-description
        self.driver.find_element(By.ID, 'input-description').click()
        # click search button
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div[3]/div/button').click()

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, element):
        """Cuộn đến một phần tử cụ thể trên trang."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)
