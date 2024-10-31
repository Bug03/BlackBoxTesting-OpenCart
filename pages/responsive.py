import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Responsive:
    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get('http://localhost:8080/opencart-site/')
        time.sleep(2)

    def get_current_url(self):
        return self.driver.current_url

    def emulate_mobile_device(self, width=375, height=667, device_scale_factor=3, mobile=True,
                              orientation='portraitPrimary'):
        """
        Mô phỏng thiết bị di động trong DevTools.

        :param width: Chiều rộng màn hình của thiết bị.
        :param height: Chiều cao màn hình của thiết bị.
        :param device_scale_factor: Hệ số thu phóng của thiết bị.
        :param mobile: Đặt True để mô phỏng thiết bị di động.
        :param orientation: Chọn 'portraitPrimary' hoặc 'landscapePrimary'.
        """
        self.driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
            'width': width,
            'height': height,
            'deviceScaleFactor': device_scale_factor,
            'mobile': mobile,
            'screenOrientation': {'angle': 0 if orientation == 'portraitPrimary' else 90, 'type': orientation}
        })
        time.sleep(2)

    def open_menu(self):
        """
        Opens the navigation menu by clicking the menu button.

        This method finds the menu button using its XPath and clicks it to open the navigation menu.
        It then waits for 2 seconds to ensure the menu is fully opened.
        """
        self.driver.find_element(By.XPATH, '//*[@id="menu"]/button').click()
        time.sleep(2)

    def get_navigation_items(self):
        """
        Retrieves all navigation items.

        This method finds all elements with the class name 'nav-item' and returns them as a list.
        """
        return self.driver.find_elements(By.CLASS_NAME, 'nav-item')

    def get_dropdown_items(self, menu_xpath, items_xpath):
        """
        Retrieves items from a dropdown menu.

        This method clicks on a menu item specified by its XPath to open the dropdown.
        It then waits for 2 seconds and finds all items within the dropdown using their XPath.

        :param menu_xpath: The XPath of the menu item to click.
        :param items_xpath: The XPath of the items within the dropdown.
        :return: A list of elements representing the dropdown items.
        """
        self.driver.find_element(By.XPATH, menu_xpath).click()
        time.sleep(2)
        return self.driver.find_elements(By.XPATH, items_xpath)

    def check_navigation(self):
        """
        Checks the navigation menu and its dropdown items.

        This method opens the navigation menu and retrieves the navigation items.
        It then retrieves the dropdown items for desktops, laptops, and components.

        :return: A tuple containing lists of navigation items, desktop items, laptop items, and component items.
        """
        self.open_menu()
        navigation = self.get_navigation_items()
        desktops = self.get_dropdown_items('/html/body/main/div[1]/nav/div[2]/ul/li[1]/a',
                                           '/html/body/main/div[1]/nav/div[2]/ul/li[1]/div/div/ul/li')
        laptops = self.get_dropdown_items('/html/body/main/div[1]/nav/div[2]/ul/li[2]/a',
                                          '/html/body/main/div[1]/nav/div[2]/ul/li[2]/div/div/ul/li')
        components = self.get_dropdown_items('/html/body/main/div[1]/nav/div[2]/ul/li[3]/a',
                                             '/html/body/main/div[1]/nav/div[2]/ul/li[3]/div/div/ul/li')
        return navigation, desktops, laptops, components
