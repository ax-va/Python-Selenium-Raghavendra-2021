import pathlib
import sys

from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, NoSuchElementException
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
from webpages.urls import GOOGLE_URL


TIMEOUT = 10  # seconds
POLLING_EVERY = 0.1  # second

driver = webdrivers.get_chromedriver()
wait = WebDriverWait(
    driver=driver,
    timeout=TIMEOUT,
    poll_frequency=POLLING_EVERY,
    ignored_exceptions=[NoSuchElementException, ElementNotVisibleException]  # exceptions ignored during calls
)
driver.get(GOOGLE_URL)

try:
    # Find element of button "Reject all"
    button_reject_all = wait.until(EC.presence_of_element_located((By.ID, "W0wltc")))
except TimeoutException:
    pass
else:
    # Click button "Reject all"
    button_reject_all.click()

try:
    # Try to find non-existent element
    non_existent = wait.until(EC.presence_of_element_located((By.ID, "Non-existent")))
except TimeoutException:
    pass

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("github ax-va")
search_bar.submit()
first_item = driver.find_element(By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
first_item.click()

driver.quit()
