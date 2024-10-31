import time
from pages.add_to_cart import AddToCart
from utils.conftest import Driver
from pages.search import Search
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class Checkout:
    def __init__(self, driver):
        self.driver = driver

    def go_to_checkout(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[5]/a").click()
        time.sleep(2)

    def prepare_product_before_checkout(self):
        add_to_cart = AddToCart(self.driver)
        search = Search(self.driver)
        search.go_to_home_page()
        search.search('iphone')
        search.scroll_to_first_product()
        add_to_cart.choose_product_by_name('iPhone')
        add_to_cart.add_to_cart_in_product_page_with_qty(2)
        add_to_cart.scroll_to_top()

    def fill_checkout_guest_details(self, first_name, last_name, email, company, address, city, post_code, country, region):
        """
        Fill checkout details as guest
        :param first_name
        :param last_name
        :param email
        :param company
        :param address
        :param city
        :param post_code
        :param country
        :param region
        """
        # click on checkout as guest
        self.click_checkout_as_guest()
        # fill personal details
        self.fill_personal_details(first_name, last_name, email)
        # fill shipping address
        self.fill_shipping_address(company, address, city, post_code, country, region)
        # click on register button
        self.register_account()
        # Check for all errors before saving details
        if not self.get_error_message('fname_not_exist') and \
                not self.get_error_message('lname_not_exist') and \
                not self.get_error_message('email_not_exist') and \
                not self.get_error_message('address_not_exist') and \
                not self.get_error_message('city_not_exist'):
            self.save_details_and_continue()

    def fill_checkout_register_details(self, first_name, last_name, email, password, company, address, city, post_code, country, region, privacy_policy=True, wish= True):
        self.click_checkout_as_register()
        self.fill_personal_details(first_name, last_name, email)
        self.fill_password(password)
        self.fill_shipping_address(company, address, city, post_code, country, region)
        if privacy_policy:
            self.agree_to_privacy_policy()

        if wish:
            # click on checkbox to subscribe to newsletter
            self.wish_to_subscribe()

        # click on register button
        self.register_account()
         # Check for all errors before saving details
        if not self.get_error_message('fname_not_exist') and \
                not self.get_error_message('lname_not_exist') and \
                not self.get_error_message('email_not_exist') and \
                not self.get_error_message('address_not_exist') and \
                not self.get_error_message('city_not_exist'):
                    self.save_details_and_continue()

    def click_checkout_as_guest(self):
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[1]/div[1]/div[2]/input').click()
        time.sleep(2)

    def fill_personal_details(self, first_name, last_name, email):
        self.scroll_to_element(self.driver.find_element(By.XPATH, '//*[@id="form-register"]/fieldset[1]/legend'))
        self.driver.find_element(By.ID, 'input-firstname').send_keys(first_name)
        self.driver.find_element(By.ID, 'input-lastname').send_keys(last_name)
        self.driver.find_element(By.ID, 'input-email').send_keys(email)

    def fill_shipping_address(self, company, address, city, post_code, country, region):
        self.scroll_to_element(self.driver.find_element(By.XPATH, '//*[@id="shipping-address"]/legend'))
        self.driver.find_element(By.ID, 'input-shipping-company').send_keys(company)
        self.driver.find_element(By.ID, 'input-shipping-address-1').send_keys(address)
        self.driver.find_element(By.ID, 'input-shipping-city').send_keys(city)
        self.driver.find_element(By.ID, 'input-shipping-postcode').send_keys(post_code)
        self.select_country_and_region(country, region)

    def select_country_and_region(self, country, region):
        select_country = Select(self.driver.find_element(By.ID, 'input-shipping-country'))
        select_country.select_by_visible_text(country)
        time.sleep(2)
        select_region = Select(self.driver.find_element(By.XPATH, '//*[@id="input-shipping-zone"]'))
        select_region.select_by_visible_text(region)
        time.sleep(2)

    def save_details_and_continue(self):
        """
        Save details and continue to next step
        """
        self.choose_shipping_method()
        self.choose_payment_method()
        self.confirm_order()

    def register_account(self):
        time.sleep(1)
        # scroll to the register button
        self.scroll_to_element(self.driver.find_element(By.ID, 'button-register'))
        self.driver.find_element(By.ID, 'button-register').click()
        time.sleep(5)

    def choose_shipping_method(self):
        self.scroll_to_element(
            self.driver.find_element(By.XPATH, '//*[@id="checkout-shipping-method"]/fieldset/legend'))
        self.driver.find_element(By.XPATH,
                                 '/html/body/main/div[2]/div/div/div/div[2]/div[1]/fieldset/div[1]/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[1]/input').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[2]/button").click()
        time.sleep(2)

    def choose_payment_method(self):
        self.driver.find_element(By.XPATH,
                                 '/html/body/main/div[2]/div/div/div/div[2]/div[2]/fieldset/div[1]/button').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/input').click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/button').click()
        time.sleep(4)

    def confirm_order(self):
        self.scroll_to_element(
            self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button'))
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[2]/div/button').click()
        time.sleep(2)

    def click_checkout_as_register(self):
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[1]/div[1]/div[1]/input').click()
        time.sleep(2)

    def fill_password(self, password):
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys(password)

    def agree_to_privacy_policy(self):
        self.driver.find_element(By.ID, 'input-register-agree').click()

    def wish_to_subscribe(self):
        self.driver.find_element(By.ID, 'input-newsletter').click()

    def scroll_to_element(self, element):
        """Cuộn đến một phần tử cụ thể trên trang."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    def get_message(self):
        # get message after checkout
        message = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/h1").text
        return message

    def get_error_message(self, error_type):
        # docs for this function
        """
        Get error message
        Args:
            error_type: error type
        Returns:
            str: error message
        """
        # XPath for each error messages
        error_xpaths = {
            'email_exist': "/html/body/div/div",
            'password_not_exist': "/html/body/main/div[2]/div/div/div/div[1]/div/form/div[1]/div[1]/fieldset/div/div/div",
            'fname_not_exist': "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[1]/div",
            'lname_not_exist': "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[2]/div",
            'address_not_exist': "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[2]/div",
            'city_not_exist': "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[2]/div/div[4]/div",
            'email_not_exist': "/html/body/main/div[2]/div/div/div/div[1]/div/form/fieldset[1]/div[2]/div[3]/div",
            'policy': "/html/body/div/div"
        }

        xpath = error_xpaths.get(error_type)
        if xpath:
            message = self.driver.find_element(By.XPATH, xpath).text
            return message
        else:
            return "Invalid error type"

