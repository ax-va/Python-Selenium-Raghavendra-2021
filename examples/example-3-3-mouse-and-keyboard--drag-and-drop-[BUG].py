"""
Selenium has bugs with drag-and-drop:
1) Positions are determined not correctly;
2) release() does not work.
"""
import os
import pathlib
import sys
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers


driver = webdrivers.get_chromedriver()
website_abspath = os.path.abspath("../websites/drag-and-drop/drag-and-drop.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

source1 = driver.find_element(By.ID, "source1")
target1 = driver.find_element(By.ID, "target1")

actions = ActionChains(driver)
# actions.drag_and_drop(source1, target1).pause(5).perform()
# actions.click_and_hold(source1).move_to_element(target1).pause(5).release().pause(5).perform()
actions.click_and_hold(source1).move_by_offset(120, 55).pause(5).release().pause(5).perform()

# Closes all the open windows and terminate the process for the driver
driver.quit()
