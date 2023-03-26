import pathlib
import sys

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


TIMEOUT = 20  # seconds

driver = webdrivers.get_chromedriver()
# Set implicit wait function for waiting TIMEOUT seconds to find or locate web elements
driver.implicitly_wait(TIMEOUT)
# Waiting is implemented by polling Document Object Model (DOM)
driver.get(GOOGLE_URL)

try:
    # Find element of button "Reject all"
    button_reject_all = driver.find_element(By.ID, "W0wltc")
except NoSuchElementException:
    pass
else:
    # Click button "Reject all"
    button_reject_all.click()

try:
    # Try to find non-existent element
    non_existent = driver.find_element(By.ID, "Non-existent")
except NoSuchElementException:
    pass

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("github ax-va")
search_bar.submit()
results_item = driver.find_element(By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
results_item.click()

driver.quit()
