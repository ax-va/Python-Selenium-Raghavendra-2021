"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute the following command:
--------------------------------------------------------------------------
python -m unittest tests.test__example_13_unitest__google_search -v
--------------------------------------------------------------------------
or discover and execute all the tests with the command:
-------------------------------
python -m unittest discover -v
-------------------------------
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
    """ Called once, before executing the module """
    pass

def tearDownModule():
    """ Called once, after executing the module """
    pass


class TestCaseGoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdrivers.get_chromedriver()
        cls.pages = Pages(cls.driver)
        cls.DIALOG_AGREEMENT = cls.pages.get("DialogAgreement")
        cls.PAGE_MAIN = cls.pages.get("PageMain")
        cls.PAGE_RESULTS = cls.pages.get("PageResults")
        locator_results_item = (By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
        cls.results_item = cls.PAGE_RESULTS.create_clickable_element(locator_results_item)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1_open_main_google_page(self):
        self.driver.get(GOOGLE_URL)
        try:
            self.DIALOG_AGREEMENT.reject_all()
        except NoSuchElementException:
            pass
        self.assertTrue(self.PAGE_MAIN.is_opened(), "Main Google page not opened")

    def test2_search_for_github(self):
        self.PAGE_MAIN.search_for("github ax-va")
        try:
            self.results_item.wait_for_presence_of_this_element_located()
        except TimeoutException:
            self.assertTrue(False, "Could not find searched item")

    def test3_open_github_page(self):
        self.results_item.click()
        time.sleep(5)
        self.assertIn("ax-va", self.driver.title, "Desired Github page not opened")

# ...
# test1_open_main_google_page (tests.test__example_13_unitest__google_search.TestCaseGoogleSearch) ... ok
# test2_search_for_github (tests.test__example_13_unitest__google_search.TestCaseGoogleSearch) ... ok
# test3_open_github_page (tests.test__example_13_unitest__google_search.TestCaseGoogleSearch) ... ok
# ...
