import pathlib
import sys
import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from webpages.urls import GOOGLE_URL


driver = webdrivers.get_chromedriver()
driver.get(GOOGLE_URL)

try:
    # Find element of button "Reject all"
    button_reject_all = driver.find_element(By.ID, "W0wltc")
except NoSuchElementException:
    pass
else:
    button_reject_all.click()

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("github ax-va")
time.sleep(5)
search_bar.submit()
time.sleep(5)
first_item = driver.find_element(By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
first_item.click()
time.sleep(5)

try:
    first_item.click()
except StaleElementReferenceException:
    print("Web element is stale")

driver.quit()
