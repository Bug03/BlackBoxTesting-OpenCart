from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'input-username')  # Update the locator as per your page
        self.password_input = (By.ID, 'input-password')  # Update the locator as per your page
        self.login_button = (By.XPATH, '//button[@type="submit"]')  # Update the locator as per your page

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[2]/div/form/div[1]/input').send_keys(username)
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[2]/div/form/div[2]/input').send_keys(password)
        self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button').click()