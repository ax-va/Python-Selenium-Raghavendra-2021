import pathlib
import sys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # Web driver waits for 2 seconds for locating the web element
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "query")))
except TimeoutException:
    # When loading the page takes some more time
    print("Take some more time for loading")

driver.quit()
