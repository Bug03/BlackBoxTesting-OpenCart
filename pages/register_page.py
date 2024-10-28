import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_register_page(self):
        self.driver.get('http://localhost:8080/opencart-site/')
        # click on My Account > Register
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[1]/a").click()
        time.sleep(2)

    def register(self, firstname, lastname, email, password, agree=True):
        self.driver.find_element(By.XPATH, '//*[@id="input-firstname"]').send_keys(firstname)
        self.driver.find_element(By.XPATH, '//*[@id="input-lastname"]').send_keys(lastname)
        self.driver.find_element(By.XPATH, '//*[@id="input-email"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="input-password"]').send_keys(password)
        # scroll view
        self.scroll_to_element(self.driver.find_element(By.NAME, 'agree'))
        time.sleep(1)

        if agree:
            self.driver.find_element(By.NAME, 'agree').click()
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)

    def get_error_message(self):
        error_elements = self.driver.find_elements(By.CLASS_NAME, 'invalid-feedback')
        error_messages = [element.text for element in error_elements]
        #  Nếu tồn tại self.driver.find_element(By.XPATH, "/html/body/div").text thì thêm vào error_messages
        if self.driver.find_elements(By.XPATH, "/html/body/div"):
            error_messages.append(self.driver.find_element(By.XPATH, "/html/body/div").text)

        email_input = self.driver.find_element(By.XPATH, '//*[@id="input-email"]')
        if email_input:
            validation_message = email_input.get_attribute('validationMessage')
            if validation_message:  # Only add if there is a validation message
                error_messages.append(validation_message)

        return error_messages

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, element):
        """Cuộn đến một phần tử cụ thể trên trang."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)



