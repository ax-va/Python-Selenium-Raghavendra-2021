import pathlib
import sys
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as e_cs
from selenium.webdriver.support.ui import WebDriverWait

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from urls.urls import WIKI_APRESS_URL


driver = webdrivers.get_chromedriver()
actions = ActionChains(driver)
driver.get(WIKI_APRESS_URL)
time.sleep(5)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).pause(5).perform()
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).pause(5).perform()

driver.get(WIKI_APRESS_URL)
time.sleep(5)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).reset_actions()
actions.perform()

driver.quit()
