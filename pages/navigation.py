import time
from selenium.webdriver.common.by import By

class Navigation:
    def __init__(self, driver):
        self.driver = driver
        self.pageName = ''

    def go_to_home_page(self):
        self.driver.get('http://localhost:8080/opencart-site/')
        time.sleep(2)

    def get_page_name(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, '.list-group-item.active')
        self.pageName = [element.text for element in elements]
        print(f"Actual Page names: {self.pageName}")
        return self.pageName

    def show_all_desktops(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[1]/a').click()
        self.driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[1]/div/a').click()
        self.get_page_name()
        time.sleep(2)

    def show_all_laptops_and_notebooks(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[2]/a').click()
        self.driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[2]/div/a').click()
        self.get_page_name()
        time.sleep(2)

    def show_all_components(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[3]/div/a').click()
        self.get_page_name()
        time.sleep(2)

    def show_all_tablets(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[4]/a').click()
        self.get_page_name()
        time.sleep(2)

    def show_all_software(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[5]/a').click()
        self.get_page_name()
        time.sleep(2)

    def show_all_phones_and_pdas(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[6]/a').click()
        self.get_page_name()
        time.sleep(2)

    def show_all_cameras(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[7]/a').click()
        self.get_page_name()
        time.sleep(2)

    def show_all_mp3_players(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[8]/a').click()
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[8]/div/a').click()
        self.get_page_name()
        time.sleep(2)

    def drop_down_inner_desktops_pc(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[1]/a').click()
        self.driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[1]/div/div/ul/li[1]/a').click()
        self.get_page_name()
        time.sleep(2)

    def drop_down_inner_desktops_mac(self):
        self.driver.find_element(By.XPATH,'/html/body/main/div[1]/nav/div[2]/ul/li[1]/a').click()
        self.driver.find_element(By.XPATH,'//*[@id="narbar-menu"]/ul/li[1]/div/div/ul/li[2]/a').click()
        self.get_page_name()
        time.sleep(2)

    def drop_down_inner_laptops_and_notebooks_macs(self):
        self.driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/div/div/ul/li[1]/a').click()
        self.get_page_name()
        time.sleep(2)

    def drop_down_inner_laptops_and_notebooks_windows(self):
        self.driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[2]/div/div/ul/li[2]/a').click()
        self.get_page_name()
        time.sleep(2)

    def drop_down_inner_components_mice_and_trackballs(self):
        self.driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[3]/div/div/ul/li[1]/a').click()
        self.get_page_name()
        time.sleep(2)

    def drop_down_inner_components_monitors(self):
        self.driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[3]/div/div/ul/li[2]/a').click()
        self.get_page_name()
        time.sleep(2)

    def drop_down_inner_components_printers(self):
        self.driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[3]/div/div/ul/li[3]/a').click()
        self.get_page_name()
        time.sleep(2)

    def drop_down_inner_components_scanners(self):
        self.driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[3]/div/div/ul/li[4]/a').click()
        self.get_page_name()
        time.sleep(2)

    def drop_down_inner_components_web_cameras(self):
        self.driver.find_element(By.XPATH, '/html/body/main/div[1]/nav/div[2]/ul/li[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="narbar-menu"]/ul/li[3]/div/div/ul/li[5]/a').click()
        self.get_page_name()
        time.sleep(2)

    def get_current_url(self):
        return self.driver.current_url