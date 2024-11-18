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
from webpages.urls import APRESS_URL


driver = webdrivers.get_geckodriver()
actions = ActionChains(driver)

driver.get(APRESS_URL)
time.sleep(5)
# Find element
menu_categories = driver.find_element(By.LINK_TEXT, "CATEGORIES")
# Move to element to open the drop-down menu
actions.move_to_element(menu_categories).perform()
# Wait 5 seconds for submenu to be displayed
WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "Python")))
# Find element
menu_python = driver.find_element(By.LINK_TEXT, "Python")
time.sleep(5)
# Click on element
menu_python.click()
time.sleep(5)

driver.get(APRESS_URL)
time.sleep(5)
# Move to position and wait
actions.move_by_offset(xoffset=268, yoffset=66).pause(5).perform()  # from the top-left corner

driver.get(APRESS_URL)
time.sleep(5)
# Find element
menu_categories = driver.find_element(By.LINK_TEXT, "CATEGORIES")
# Move to element with offset, wait, click, wait
actions.move_to_element_with_offset(menu_categories, 200, 50).pause(5).click().pause(5).perform()

# Closes all the open windows and terminate the process for the driver
driver.quit()
