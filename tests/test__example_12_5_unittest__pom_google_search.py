"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute one of the following commands:
---------------------------------------------------------------------------
python -m unittest -v tests.test__example_12_5_unittest__pom_google_search
python3 -m unittest -v tests.test__example_12_5_unittest__pom_google_search
---------------------------------------------------------------------------

or discover and execute all the found tests with the commands:
-------------------------------
python -m unittest discover -v
python3 -m unittest discover -v
-------------------------------
"""
import os
import pathlib
import sys
import unittest
import time

from datetime import datetime
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from pom_google_search.pages import Pages
from utils.highlighter import Highlighter
from utils.screenshot_maker import ScreenshotMaker
from webpages.urls import GOOGLE_URL


def setUpModule():
    pass


def tearDownModule():
    pass


class TestCaseGoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdrivers.get_chromedriver()
        # Create a POM page controller
        cls.pages = Pages(cls.driver)
        # Create a screenshots' directory
        tests_dir = str(pathlib.Path(__file__).resolve().parents[0])
        timestamp = datetime.now().strftime("date-%y-%m-%d-time-%H-%M-%S-%f")
        screenshots_dir = os.path.join(tests_dir, "screenshots-" + timestamp)
        os.mkdir(screenshots_dir)
        # Create a screenshot maker
        cls.sm = ScreenshotMaker(cls.driver, screenshots_dir)
        # Create a highlighter
        cls.highlighter = Highlighter(cls.driver, border="")
        # Get POM pages
        cls.DIALOG_AGREEMENT = cls.pages.get("DialogAgreement")
        cls.PAGE_MAIN = cls.pages.get("PageMain")
        cls.PAGE_RESULTS = cls.pages.get("PageResults")
        # Create POM clickable elements on page PAGE_RESULTS
        locator_for_results_item = (By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
        cls.results_item = cls.PAGE_RESULTS.create_clickable_element(locator_for_results_item)
        locator_for_non_existent_item = (By.ID, "Non-existent")
        cls.non_existent_item = cls.PAGE_RESULTS.create_clickable_element(locator_for_non_existent_item)
        # Set parameters to skip tests
        cls.is_main_google_page_ready = False
        cls.is_search_for_github_successful = False

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1_open_main_google_page(self):
        # Execute test itself
        self.driver.get(GOOGLE_URL)
        self.sm.make_screenshot("Google-URL-opened")
        try:
            self.DIALOG_AGREEMENT.reject_all()
            self.sm.make_screenshot("all-rejected-on-dialog-agreement")
        except NoSuchElementException:
            pass
        self.assertTrue(self.PAGE_MAIN.is_ready(), "Main Google page not ready")
        # Set that the test has been successful
        self.__class__.is_main_google_page_ready = True

    def test2_search_for_github(self):
        # Skip if preconditions are not satisfied
        self.skip_if_main_page_not_ready()
        # Execute test itself
        self.PAGE_MAIN.part_search_bar.element_input.send_keys("github ax-va")
        self.sm.make_screenshot("request-typed")
        self.PAGE_MAIN.part_search_bar.element_input.submit()
        self.sm.make_screenshot("request-submitted")
        # Ensure the searched item is visible to click it
        try:
            self.results_item.wait_for_presence_of_this_element_located()
        except TimeoutException as e:
            self.fail(f"{e.__class__.__name__}: element not found")
        else:
            self.highlighter.highlight(self.results_item.find_this_element())
            self.sm.make_screenshot("found-item-highlighted")
        # Set that the test has been successful
        self.__class__.is_search_for_github_successful = True

    def test3_check_for_non_existent_item(self):
        # Ensure the non-existent item does not exist
        self.assertRaises(TimeoutException, self.non_existent_item.wait_for_presence_of_this_element_located)

    def test4_open_github_page(self):
        # Skip if preconditions are not satisfied
        self.skip_if_main_page_not_ready()
        self.skip_if_search_for_github_not_successful()
        # Execute test itself
        self.results_item.click()
        self.sm.make_screenshot("found-item-clicked")
        time.sleep(5)
        self.assertIn("ax-va", self.driver.title, "Desired Github page not opened")

    def skip_if_main_page_not_ready(self):
        if not self.__class__.is_main_google_page_ready:
            self.skipTest("Main Google page not ready")

    def skip_if_search_for_github_not_successful(self):
        if not self.__class__.is_search_for_github_successful:
            self.skipTest("Search for Github not successful")


# test1_open_main_google_page (tests.test__example_12_5_unittest__pom_google_search.TestCaseGoogleSearch) ... ok
# test2_search_for_github (tests.test__example_12_5_unittest__pom_google_search.TestCaseGoogleSearch) ... ok
# test3_check_for_non_existent_item (tests.test__example_12_5_unittest__pom_google_search.TestCaseGoogleSearch) ... ok
# test4_open_github_page (tests.test__example_12_5_unittest__pom_google_search.TestCaseGoogleSearch) ... ok
# ...
