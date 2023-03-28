import pathlib
import sys
import time

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

driver = webdrivers.get_chromedriver()
# Create a POM page controller
pages = Pages(driver)
# Get POM pages
DIALOG_AGREEMENT = pages.get("DialogAgreement")
PAGE_MAIN = pages.get("PageMain")
PAGE_RESULTS = pages.get("PageResults")

driver.get(GOOGLE_URL)
try:
    DIALOG_AGREEMENT.reject_all()
except NoSuchElementException:
    pass
PAGE_MAIN.search_for("github ax-va")
# Create POM clickable elements on page PAGE_RESULTS
non_existent = PAGE_RESULTS.create_clickable_element((By.ID, "Non-existent"))
results_item = PAGE_RESULTS.create_clickable_element((By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]"))
# The non-existent item does not exist
try:
    non_existent.wait_for_presence_of_this_element_located()
except TimeoutException:
    pass
# Ensure the searched item is visible to click it
results_item.wait_for_presence_of_this_element_located()
results_item.click()
time.sleep(5)

driver.quit()
