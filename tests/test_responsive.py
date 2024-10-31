from utils.conftest import Driver
from pages.responsive import Responsive
import pytest

class TestResponsive(Driver):
    @pytest.mark.parametrize('driver', [True], indirect=True)
    def test_emulate_mobile_device(self, driver):
        """
        Test emulating a mobile device.

        Steps:
        1. Navigate to the home page.
        2. Emulate a mobile device with specified dimensions and scale factor.

        Args:
            driver: WebDriver instance.
        """
        responsive = Responsive(driver)
        responsive.go_to_home_page()
        responsive.emulate_mobile_device(width=375, height=812, device_scale_factor=3)

    @pytest.mark.parametrize('driver', [True], indirect=True)
    def test_check_navigation_in_mobile_device(self, driver):
        """
        Test checking navigation items on a mobile device.

        Steps:
            1. Navigate to the home page.
            2. Emulate a mobile device with specified dimensions and scale factor.
            3. Check the navigation items and their dropdowns.

        Args:
            driver: WebDriver instance.
        """
        responsive = Responsive(driver)
        responsive.go_to_home_page()
        responsive.emulate_mobile_device(width=375, height=812, device_scale_factor=3)

        navigation, desktops, laptops, components = responsive.check_navigation()
        assert len(navigation) == 8
        assert len(desktops) == 2
        assert len(laptops) == 2
        assert len(components) == 5

    @pytest.mark.parametrize('driver', [True], indirect=True)
    def test_check_navigation_in_tablet_device(self, driver):
        """
        Test checking navigation items on a tablet device.

        Steps:
            1. Navigate to the home page.
            2. Emulate a tablet device with specified dimensions and scale factor.
            3. Check the navigation items and their dropdowns.

        Args:
            driver: WebDriver instance.
        """
        responsive = Responsive(driver)
        responsive.go_to_home_page()
        responsive.emulate_mobile_device(width=768, height=1024, device_scale_factor=2)

        navigation, desktops, laptops, components = responsive.check_navigation()
        assert len(navigation) == 8
        assert len(desktops) == 2
        assert len(laptops) == 2
        assert len(components) == 5

    @pytest.mark.parametrize('driver', [True], indirect=True)
    def test_search_in_mobile_device(self, driver):
        """
        Test search functionality on a mobile device.

        Steps:
            1. Navigate to the home page.
            2. Emulate a mobile device with specified dimensions and scale factor.
            3. Perform search tests.

        Args:
            driver: WebDriver instance.
        """
        responsive = Responsive(driver)
        responsive.go_to_home_page()
        responsive.emulate_mobile_device(width=375, height=812, device_scale_factor=3)

        from tests.test_search import TestSearch
        search = TestSearch()

        # if search.test_search(driver) is working then this test will work
        search.test_search(driver)
        assert True, "test_search_in_mobile_device is working"

    @pytest.mark.parametrize('driver', [True], indirect=True)
    def test_search_description_in_mobile_device(self, driver):
        """
        Test search functionality with description on a mobile device.

        Steps:
            1. Navigate to the home page.
            2. Emulate a mobile device with specified dimensions and scale factor.
            3. Perform search tests with description.

        Args:
            driver: WebDriver instance.
        """
        responsive = Responsive(driver)
        responsive.go_to_home_page()
        responsive.emulate_mobile_device(width=375, height=812, device_scale_factor=3)

        from tests.test_search import TestSearch
        search = TestSearch()

        # if search.test_search_description(driver) is working then this test will work
        search.test_search_description(driver)
        assert True, "test_search_description_in_mobile_device is working"

    @pytest.mark.parametrize('driver', [True], indirect=True)
    def test_search_in_tablet_device(self, driver):
        """
        Test search functionality on a tablet device.

        Steps:
        1. Navigate to the home page.
        2. Emulate a tablet device with specified dimensions and scale factor.
        3. Perform search tests.

        Args:
            driver: WebDriver instance.
        """
        responsive = Responsive(driver)
        responsive.go_to_home_page()
        responsive.emulate_mobile_device(width=768, height=1024, device_scale_factor=2)

        from tests.test_search import TestSearch
        search = TestSearch()

        # if search.test_search(driver) is working then this test will work
        search.test_search(driver)
        assert True, "test_search_in_tablet_device is working"

    @pytest.mark.parametrize('driver', [True], indirect=True)
    def test_search_description_in_tablet_device(self, driver):
        """
        Test search functionality with description on a tablet device.

        Steps:
            1. Navigate to the home page.
            2. Emulate a tablet device with specified dimensions and scale factor.
            3. Perform search tests with description.

        Args:
            driver: WebDriver instance.
        """

        responsive = Responsive(driver)
        responsive.go_to_home_page()
        responsive.emulate_mobile_device(width=768, height=1024, device_scale_factor=2)

        from tests.test_search import TestSearch
        search = TestSearch()

        # if search.test_search_description(driver) is working then this test will work
        search.test_search_description(driver)
        assert True, "test_search_description_in_tablet_device is working"






