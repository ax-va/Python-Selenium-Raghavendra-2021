import os
import pathlib
import sys
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from utils.highlighter import Highlighter


driver = webdrivers.get_chromedriver()
highlighter = Highlighter(driver)
actions = ActionChains(driver)
website_abspath = os.path.abspath("../webpages/radio-buttons/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# Select 'diverse' radio button
radio_button_other = driver.find_element(By.ID, "other")
radio_button_other.click()
time.sleep(5)

radio_button_female = driver.find_element(By.ID, "female")
radio_button_female.click()
time.sleep(5)

assert radio_button_female.is_selected() is True  # correct
assert radio_button_female.get_attribute("checked") == "true"  # correct
assert radio_button_other.is_selected() is False  # correct
assert radio_button_other.get_attribute("checked") != "true"  # correct
assert radio_button_other.get_attribute("checked") is None  # correct

driver.quit()
