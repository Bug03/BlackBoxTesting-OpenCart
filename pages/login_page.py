import time

from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.get('http://localhost:8080/opencart-site/')
        # click on My Account > Login
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()
        time.sleep(2)

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[2]/div/form/div[1]/input').send_keys(username)
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[2]/div/form/div[2]/input').send_keys(password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)

    def logout(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[5]/a").click()
        time.sleep(2)

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div").text

    def get_current_url(self):
        return self.driver.current_url
