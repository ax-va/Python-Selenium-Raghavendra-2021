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


driver = webdrivers.get_geckodriver()
actions = ActionChains(driver)

driver.get("http://www.apress.com")
time.sleep(5)
# Find element
menu_categories = driver.find_element(By.LINK_TEXT, "CATEGORIES")
# Move to element to open the panel
actions.move_to_element(menu_categories).perform()
# Wait for sub menu to be displayed
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "Python")))
# Find element
menu_python = driver.find_element(By.LINK_TEXT, "Python")
time.sleep(5)
# Click on element
menu_python.click()
time.sleep(5)

# Closes all the open windows and terminate the process for the driver
driver.quit()
