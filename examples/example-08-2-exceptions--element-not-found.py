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
from webpages.urls import APRESS_URL


driver = webdrivers.get_chromedriver()
driver.get(APRESS_URL)

try:
    privacy = driver.find_element(By.ID, "privacy")
except NoSuchElementException:
    print(f"Web element cannot be found")
else:
    privacy.click()
    time.sleep(5)

driver.quit()
