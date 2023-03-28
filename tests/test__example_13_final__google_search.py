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
        # Create a POM page controller
        cls.pages = Pages(cls.driver)
        # Get POM pages
        cls.DIALOG_AGREEMENT = cls.pages.get("DialogAgreement")
        cls.PAGE_MAIN = cls.pages.get("PageMain")
        cls.PAGE_RESULTS = cls.pages.get("PageResults")
        # Create POM clickable elements on page PAGE_RESULTS to click them later
        locator_for_results_item = (By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
        cls.results_item = cls.PAGE_RESULTS.create_clickable_element(locator_for_results_item)
        locator_for_non_existent = (By.ID, "Non-existent")
        cls.non_existent = cls.PAGE_RESULTS.create_clickable_element(locator_for_non_existent)
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
        try:
            self.DIALOG_AGREEMENT.reject_all()
        except NoSuchElementException:
            pass
        self.assertTrue(self.PAGE_MAIN.is_ready(), "Main Google page not ready")
        # Set that the test has been successful
        self.__class__.is_main_google_page_ready = True

    def test2_search_for_github(self):
        # Skip if preconditions are not satisfied
        self.skip_if_main_page_not_ready()
        # Execute test itself
        self.PAGE_MAIN.search_for("github ax-va")
        # Ensure the searched item is visible to click it
        self.results_item.wait_for_presence_of_this_element_located()
        # Set that the test has been successful
        self.__class__.is_search_for_github_successful = True

    def test3_check_for_non_existent_item(self):
        # Ensure the non-existent item does not exist
        self.assertRaises(TimeoutException, self.non_existent.wait_for_presence_of_this_element_located)

    def test4_open_github_page(self):
        # Skip if preconditions are not satisfied
        self.skip_if_main_page_not_ready()
        self.skip_if_search_for_github_not_successful()
        # Execute test itself
        self.results_item.click()
        time.sleep(5)
        self.assertIn("ax-va", self.driver.title, "Desired Github page not opened")

    def skip_if_main_page_not_ready(self):
        if not self.__class__.is_main_google_page_ready:
            self.skipTest("Main Google page not ready")

    def skip_if_search_for_github_not_successful(self):
        if not self.__class__.is_search_for_github_successful:
            self.skipTest("Search for Github not successful")


# test1_open_main_google_page (tests.test__example_13_final__google_search.TestCaseGoogleSearch) ... ok
# test2_search_for_github (tests.test__example_13_final__google_search.TestCaseGoogleSearch) ... ok
# test3_check_for_non_existent_item (tests.test__example_13_final__google_search.TestCaseGoogleSearch) ... ok
# test4_open_github_page (tests.test__example_13_final__google_search.TestCaseGoogleSearch) ... ok
# ...
