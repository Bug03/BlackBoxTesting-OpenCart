import time

from pages.navigation import Navigation
from utils.conftest import Driver
import re

class TestNavigation(Driver):
    def test_drop_down_inner_desktops(self, driver):
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("Desktops (1)", navigation.show_all_desktops, 1),
            ("PC (0)", navigation.drop_down_inner_desktops_pc, 0),
            ("Mac (1)", navigation.drop_down_inner_desktops_mac, 1)
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

    def test_drop_down_inner_laptops_and_notebooks(self, driver):
        navigation = Navigation(driver)
        navigation.go_to_home_page()

        test_cases = [
            ("Laptops & Notebooks (5)", navigation.show_all_laptops_and_notebooks, 5),
            ("Macs (3)", navigation.drop_down_inner_laptops_and_notebooks_macs, 3),
            ("Windows (2)", navigation.drop_down_inner_laptops_and_notebooks_windows, 2)
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

    def test_drop_down_inner_components(self, driver):
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

    def test_show_all_tablets(self, driver):
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
