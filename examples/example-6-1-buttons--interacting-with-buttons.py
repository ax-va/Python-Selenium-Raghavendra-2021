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
website_abspath = os.path.abspath("../webpages/buttons/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

default_button = driver.find_element(By.ID, "default_btn")
if default_button.is_displayed():
    print("Default Button is present")
else:
    print("Default Button is not present")

if default_button.is_enabled():
    print("Default Button is enabled")
else:
    print("Default Button is not enabled")

submit_button = driver.find_element(By.XPATH, "//*[@type='submit']")
if submit_button.is_displayed():
    print("Submit Button is present")
else:
    print("Submit Button is not present")

if submit_button.is_enabled():
    print("Submit Button is enabled")
else:
    print("Submit Button is not enabled")

# click 1
default_button.click()  # returns None
time.sleep(5)
# click 2
driver.find_element(By.ID, "default_btn").click()  # returns None
time.sleep(5)
# click 3
actions.move_to_element(default_button).pause(5).click().pause(5).perform()
# click 4
default_button = driver.find_element(By.XPATH, "//button[text()='Default Button']")
default_button.click()  # returns None
time.sleep(5)
# click 5
default_button = driver.find_element(By.NAME, "dft_btn")
default_button.click()  # returns None
time.sleep(5)

driver.quit()
