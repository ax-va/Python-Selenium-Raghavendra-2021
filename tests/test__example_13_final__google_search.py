"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute the following command:
-----------------------------------------------------------------
python -m unittest -v tests.test__example_13_final__google_search
-----------------------------------------------------------------

or discover and execute all the found tests with the command:
------------------------------
python -m unittest discover -v
------------------------------
"""
import time
import unittest
import pathlib
import sys

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from webpages.urls import GOOGLE_URL
from pom_google_search.pages import Pages


def setUpModule():
    pass


def tearDownModule():
    pass


class TestCaseGoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdrivers.get_chromedriver()
        # Create a POM page creator
        cls.pages = Pages(cls.driver)
        # Get POM pages
        cls.DIALOG_AGREEMENT = cls.pages.get("DialogAgreement")
        cls.PAGE_MAIN = cls.pages.get("PageMain")
        cls.PAGE_RESULTS = cls.pages.get("PageResults")
        # Create a POM clickable element on page PAGE_RESULTS to click it later
        locator_results_item = (By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
        cls.results_item = cls.PAGE_RESULTS.create_clickable_element(locator_results_item)
        # Set parameters to skip tests
        cls.is_test1_open_main_google_page_successful = False
        cls.is_test2_search_for_github_successful = False

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1_open_main_google_page(self):
        # Execute test
        self.driver.get(GOOGLE_URL)
        try:
            self.DIALOG_AGREEMENT.reject_all()
        except NoSuchElementException:
            pass
        self.assertTrue(self.PAGE_MAIN.is_opened(), "Main Google page not opened")
        # Set that the test has been successful
        self.__class__.is_test1_open_main_google_page_successful = True

    def test2_search_for_github(self):
        # Skip if the previous test has been not successful
        if not self.__class__.is_test1_open_main_google_page_successful:
            self.skipTest("test1_open_main_google_page not successful")
        # Execute test
        self.PAGE_MAIN.search_for("github ax-va")
        try:
            self.results_item.wait_for_presence_of_this_element_located()
        except TimeoutException:
            self.assertTrue(False, "Could not find searched item")
        # Set that the test has been successful
        self.__class__.is_test2_search_for_github_successful = True

    def test3_open_github_page(self):
        # Skip if the previous tests have been not successful
        if not self.__class__.is_test1_open_main_google_page_successful:
            self.skipTest("test1_open_main_google_page not successful")
        elif not self.__class__.is_test2_search_for_github_successful:
            self.skipTest("test2_search_for_github not successful")
        # Execute test
        self.results_item.click()
        time.sleep(5)
        self.assertIn("ax-va", self.driver.title, "Desired Github page not opened")

# ...
# test1_open_main_google_page (tests.test__example_13_unitest__google_search.TestCaseGoogleSearch) ... ok
# test2_search_for_github (tests.test__example_13_unitest__google_search.TestCaseGoogleSearch) ... ok
# test3_open_github_page (tests.test__example_13_unitest__google_search.TestCaseGoogleSearch) ... ok
# ...
