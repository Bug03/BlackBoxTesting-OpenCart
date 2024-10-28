import time

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from utils.conftest import Driver


class TestLogin(Driver):
    def test_login(self, driver):
        driver.get('http://localhost:8080/opencart-site/')
        time.sleep(2)
        # click on My Account > Login
        driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a").click()
        driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a").click()

        login_page = LoginPage(driver)
        time.sleep(2)
        login_page.login('nchd03112003@gmail.com', '1234')
        time.sleep(2)
        # index.php?route=account/account
        assert "account/account" in driver.current_url







