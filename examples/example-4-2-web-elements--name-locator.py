import os
import pathlib
import sys
import time

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
website_abspath = os.path.abspath("../webpages/employee-form/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

input_fname = driver.find_element(By.NAME, "fname")
highlighter.highlight_and_wait(input_fname)

input_email = driver.find_element(By.NAME, "email")
highlighter.highlight_and_wait(input_email)

# If multiple elements have the same attribute, then the first matched is returned
input_next = driver.find_element(By.NAME, "next")
highlighter.highlight_and_wait(input_next)

driver.quit()
