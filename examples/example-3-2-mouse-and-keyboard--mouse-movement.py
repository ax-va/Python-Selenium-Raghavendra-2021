import pathlib
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers


GITHUB_URL = "https://github.com/ax-va/Selenium4-Raghavendra-2021"

driver = webdrivers.get_geckodriver()
actions = ActionChains(driver)
# Open my GitHub URL
driver.get(GITHUB_URL)
time.sleep(5)
# Find element of "main branch"
main_branch = driver.find_element(By.XPATH, "//*[@class='btn css-truncate']")

actions.move_to_element(main_branch).pause(5).perform()

WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "Switch branches or tags")))
