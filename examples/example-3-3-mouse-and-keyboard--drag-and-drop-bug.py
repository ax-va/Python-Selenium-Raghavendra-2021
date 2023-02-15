import os
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


driver = webdrivers.get_chromedriver()
actions = ActionChains(driver)
drag_and_drop_abspath = os.path.abspath("../websites/drag-and-drop/drag-and-drop.html")
# Navigate to page stored as local file
driver.get("file:///" + drag_and_drop_abspath)
time.sleep(5)
# Locate source element
source = driver.find_element(By.ID, "drag1")
# Locate target element
target = driver.find_element(By.ID, "div1")
# Perform drag and drop action and wait
actions.drag_and_drop(source, target).pause(5).perform()
# actions.click_and_hold(source).pause(5).move_by_offset(xoffset=500, yoffset=500).pause(5).perform()

# Closes all the open windows and terminate the process for the driver
driver.quit()
