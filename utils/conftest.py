import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    @pytest.fixture(scope="function")
    def driver(self, request):
        open_dev_tools = request.param if hasattr(request, 'param') else False
        options = webdriver.ChromeOptions()

        # Only open DevTools when the parameter open_dev_tools is True
        if open_dev_tools:
            options.add_argument("--auto-open-devtools-for-tabs")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.maximize_window()

        # Example: Set up DevTools Protocol if needed
        driver.execute_cdp_cmd("Network.enable", {})
        driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*.png", "*.jpg"]})

        yield driver
        driver.quit()