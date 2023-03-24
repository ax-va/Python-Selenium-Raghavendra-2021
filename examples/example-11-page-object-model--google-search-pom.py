import pathlib
import sys
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from webpages.urls import GOOGLE_URL
from google_search_pom.controller import Controller

driver = webdrivers.get_chromedriver()
driver.get(GOOGLE_URL)

controller = Controller(driver)
AGREEMENT_DIALOG = controller.get_page("AgreementDialog")
MAIN_PAGE = controller.get_page("MainPage")
RESULTS_PAGE = controller.get_page("ResultsPage")

try:
    AGREEMENT_DIALOG.click_on_reject_all_button()
except NoSuchElementException:
    pass
MAIN_PAGE.search_for("github ax-va")
first_item = RESULTS_PAGE.wait_for_presence_of_element_located((By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]"))
clickable_item = first_item.to_clickable_element()
clickable_item.click()
time.sleep(5)

driver.quit()
