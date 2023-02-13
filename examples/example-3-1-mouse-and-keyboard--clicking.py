import pathlib
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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
# Click on element
main_branch.click()
time.sleep(5)
# Click on element again to close it
actions.click(main_branch).pause(5).perform()
# Click on element and hold (without releasing), then release
actions.click_and_hold(main_branch).pause(5).release().pause(5).perform()
# Double-click
actions.double_click(main_branch).pause(5).perform()
# Right-click to open context menu
actions.context_click(main_branch).pause(5).perform()
# TODO: How to close context menu?

# Closes all the open windows and terminate the process for the driver
driver.quit()
