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
highlighter = Highlighter(driver, wait_in_sec=2)
website_abspath = os.path.abspath("../webpages/apress/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

tag1 = driver.find_element(By.TAG_NAME, "title")
tag2 = driver.find_element(By.TAG_NAME, "h1")
highlighter.highlight_and_wait(tag2)

driver.quit()
