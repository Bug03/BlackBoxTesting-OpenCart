import time

from pages.navigation import Navigation
from utils.conftest import Driver
import re

class TestNavigation(Driver):
    def test_drop_down_inner_desktops(self, driver):
        """
        Test the drop down inner desktops navigation
        Notes:
             Steps:
                1. Go to the home page
                2. Click on Desktops > Show All Desktops
                3. Verify the page name and the number of products
                4. Click on Desktops > PC
                5. Verify the page name and the number of products
                6. Click on Desktops > Mac
                7. Verify the page name and the number of products
             Expected results:
                - The page name should match the expected page name
                - The number of products should match the expected number of products
                - The URL should contain "product/category"
        """
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("Desktops (1)", navigation.show_all_desktops, 1),
            ("PC (0)", navigation.drop_down_inner_desktops_pc, 0),
            ("Mac (1)", navigation.drop_down_inner_desktops_mac, 1)
        ]

        errors = []

        for expected_page_name, method, expected_count in test_cases:
            method()
            page_name = navigation.pageName
            print("Expected page name: ", expected_page_name)

            # Extract the number of products from the actual page name string
            product_count = 0
            for name in page_name:
                if expected_page_name.split(' (')[0] in name:
                    match = re.search(r'\((\d+)\)', name)
                    if match:
                        product_count = int(match.group(1))
                        break

            try:
                assert product_count == expected_count, f"Expected {expected_count} products for {expected_page_name}, but found {product_count}."
                assert "product/category" in navigation.get_current_url()
            except AssertionError as e:
                errors.append(f"Assertion error for {expected_page_name}: {e}")

        if errors:
            raise AssertionError("Errors occurred:\n" + "\n".join(errors))

    def test_drop_down_inner_laptops_and_notebooks(self, driver):
        """
        Test the drop down inner laptops and notebooks navigation
        Notes:
                Steps:
                    1. Go to the home page
                    2. Click on Laptops & Notebooks > Show All Laptops & Notebooks
                    3. Verify the page name and the number of products
                    4. Click on Laptops & Notebooks > Macs
                    5. Verify the page name and the number of products
                    6. Click on Laptops & Notebooks > Windows
                    7. Verify the page name and the number of products
                Expected results:
                    - The page name should match the expected page name
                    - The number of products should match the expected number of products
                    - The URL should contain "product/category"
        """
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("Laptops & Notebooks (5)", navigation.show_all_laptops_and_notebooks, 5),
            ("Macs (3)", navigation.drop_down_inner_laptops_and_notebooks_macs, 3),
            ("Windows (2)", navigation.drop_down_inner_laptops_and_notebooks_windows, 2)
        ]

        errors = []

        for expected_page_name, method, expected_count in test_cases:
            method()
            page_name = navigation.pageName
            print("Expected page name: ", expected_page_name)

            # Extract the number of products from the actual page name string
            product_count = 0
            for name in page_name:
                if expected_page_name.split(' (')[0] in name:
                    match = re.search(r'\((\d+)\)', name)
                    if match:
                        product_count = int(match.group(1))
                        break

            try:
                assert product_count == expected_count, f"Expected {expected_count} products for {expected_page_name}, but found {product_count}."
                assert "product/category" in navigation.get_current_url()
            except AssertionError as e:
                errors.append(f"Assertion error for {expected_page_name}: {e}")

        if errors:
            raise AssertionError("Errors occurred:\n" + "\n".join(errors))

    def test_drop_down_inner_components(self, driver):
        """
        Test the drop down inner components navigation
        Notes:
            Steps:
                1. Go to the home page
                2. Click on Components > Show All Components
                3. Verify the page name and the number of products
                4. Click on Components > Mice and Trackballs
                5. Verify the page name and the number of products
                6. Click on Components > Monitors
                7. Verify the page name and the number of products
                8. Click on Components > Printers
                9. Verify the page name and the number of products
                10. Click on Components > Scanners
                11. Verify the page name and the number of products
                12. Click on Components > Web Cameras
                13. Verify the page name and the number of products
            Expected results:
                - The page name should match the expected page name
                - The number of products should match the expected number of products
                - The URL should contain "product/category"
        """
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("Components (2)", navigation.show_all_components, 2),
            ("Mice and Trackballs (0)", navigation.drop_down_inner_components_mice_and_trackballs, 0),
            ("Monitors (2)", navigation.drop_down_inner_components_monitors, 2),
            ("Printers (0)", navigation.drop_down_inner_components_printers, 0),
            ("Scanners (0)", navigation.drop_down_inner_components_scanners, 0),
            ("Web Cameras (0)", navigation.drop_down_inner_components_web_cameras, 0)
        ]

        for expected_page_name, method, expected_count in test_cases:
            method()
            page_name = navigation.pageName
            print("Expected page name: ", expected_page_name)

            # Extract the number of products from the actual page name string
            product_count = 0
            for name in page_name:
                if expected_page_name.split(' (')[0] in name:
                    match = re.search(r'\((\d+)\)', name)
                    if match:
                        product_count = int(match.group(1))
                        break

            assert product_count == expected_count, f"Expected {expected_count} products for {expected_page_name}, but found {product_count}."
            assert "product/category" in navigation.get_current_url()

    def test_show_all_tablets(self, driver):
        """
        Test the show all tablets navigation
        Notes:
            Steps:
                1. Go to the home page
                2. Click on Tablets > Show All Tablets
                3. Verify the page name and the number of products
            Expected results:
                - The page name should match the expected page name
                - The number of products should match the expected number of products
                - The URL should contain "product/category"
        """
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("Tablets (1)", navigation.show_all_tablets, 1)
        ]

        for expected_page_name, method, expected_count in test_cases:
            try:
                method()
                page_name = navigation.pageName
                print("Expected page name: ", expected_page_name)

                # Extract the number of products from the actual page name string
                product_count = 0
                for name in page_name:
                    if expected_page_name.split(' (')[0] in name:
                        match = re.search(r'\((\d+)\)', name)
                        if match:
                            product_count = int(match.group(1))
                            break

                assert product_count == expected_count, f"Expected {expected_count} products for {expected_page_name}, but found {product_count}."
                assert "product/category" in navigation.get_current_url()
            except AssertionError as e:
                print(f"Assertion error for {expected_page_name}: {e}")

    def test_show_all_software(self, driver):
        """
        Test the show all software navigation
        Notes:
            Steps:
                1. Go to the home page
                2. Click on Software > Show All Software
                3. Verify the page name and the number of products
            Expected results:
                - The page name should match the expected page name
                - The number of products should match the expected number of products
                - The URL should contain "product/category"
        """
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("Software (0)", navigation.show_all_software, 0)
        ]

        for expected_page_name, method, expected_count in test_cases:
            try:
                method()
                page_name = navigation.pageName
                print("Expected page name: ", expected_page_name)

                # Extract the number of products from the actual page name string
                product_count = 0
                for name in page_name:
                    if expected_page_name.split(' (')[0] in name:
                        match = re.search(r'\((\d+)\)', name)
                        if match:
                            product_count = int(match.group(1))
                            break

                assert product_count == expected_count, f"Expected {expected_count} products for {expected_page_name}, but found {product_count}."
                assert "product/category" in navigation.get_current_url()
            except AssertionError as e:
                print(f"Assertion error for {expected_page_name}: {e}")

    def test_show_all_phones_and_pdas(self, driver):
        """
        Test the show all phones and pdas navigation
        Notes:
            Steps:
                1. Go to the home page
                2. Click on Phones & PDAs > Show All Phones & PDAs
                3. Verify the page name and the number of products
            Expected results:
                - The page name should match the expected page name
                - The number of products should match the expected number of products
                - The URL should contain "product/category"
        """
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("Phones & PDAs (3)", navigation.show_all_phones_and_pdas, 3)
        ]

        for expected_page_name, method, expected_count in test_cases:
            try:
                method()
                page_name = navigation.pageName
                print("Expected page name: ", expected_page_name)

                # Extract the number of products from the actual page name string
                product_count = 0
                for name in page_name:
                    if expected_page_name.split(' (')[0] in name:
                        match = re.search(r'\((\d+)\)', name)
                        if match:
                            product_count = int(match.group(1))
                            break

                assert product_count == expected_count, f"Expected {expected_count} products for {expected_page_name}, but found {product_count}."
                assert "product/category" in navigation.get_current_url()
            except AssertionError as e:
                print(f"Assertion error for {expected_page_name}: {e}")

    def test_show_all_cameras(self, driver):
        """
        Test the show all cameras navigation
        Notes:
            Steps:
                1. Go to the home page
                2. Click on Cameras > Show All Cameras
                3. Verify the page name and the number of products
            Expected results:
                - The page name should match the expected page name
                - The number of products should match the expected number of products
                - The URL should contain "product/category"
        """
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("Cameras (2)", navigation.show_all_cameras, 2)
        ]

        for expected_page_name, method, expected_count in test_cases:
            try:
                method()
                page_name = navigation.pageName
                print("Expected page name: ", expected_page_name)

                # Extract the number of products from the actual page name string
                product_count = 0
                for name in page_name:
                    if expected_page_name.split(' (')[0] in name:
                        match = re.search(r'\((\d+)\)', name)
                        if match:
                            product_count = int(match.group(1))
                            break

                assert product_count == expected_count, f"Expected {expected_count} products for {expected_page_name}, but found {product_count}."
                assert "product/category" in navigation.get_current_url()
            except AssertionError as e:
                print(f"Assertion error for {expected_page_name}: {e}")

    def test_show_all_mp3_players(self, driver):
        """
        Test the show all mp3 players navigation
        Notes:
            Steps:
                1. Go to the home page
                2. Click on MP3 Players > Show All MP3 Players
                3. Verify the page name and the number of products
            Expected results:
                - The page name should match the expected page name
                - The number of products should match the expected number of products
                - The URL should contain "product/category"
        """
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("MP3 Players (4)", navigation.show_all_mp3_players, 4)
        ]

        for expected_page_name, method, expected_count in test_cases:
            try:
                method()
                page_name = navigation.pageName
                print("Expected page name: ", expected_page_name)

                # Extract the number of products from the actual page name string
                product_count = 0
                for name in page_name:
                    if expected_page_name.split(' (')[0] in name:
                        match = re.search(r'\((\d+)\)', name)
                        if match:
                            product_count = int(match.group(1))
                            break

                assert product_count == expected_count, f"Expected {expected_count} products for {expected_page_name}, but found {product_count}."
                assert "product/category" in navigation.get_current_url()
            except AssertionError as e:
                print(f"Assertion error for {expected_page_name}: {e}")
