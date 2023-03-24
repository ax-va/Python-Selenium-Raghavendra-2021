import pathlib
import sys
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from webpages.urls import WIKI_URL


driver = webdrivers.get_chromedriver()
actions = ActionChains(driver)
driver.get(WIKI_URL)
time.sleep(5)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).pause(5).perform()
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).pause(5).perform()

driver.get(WIKI_URL)
time.sleep(5)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).reset_actions()
actions.perform()

button_search = driver.find_element(By.XPATH, "//*[contains(@class, 'button') and contains(@class, 'search-toggle')]")
if button_search.is_displayed():
    actions.click(button_search).pause(5).perform()

input_search = driver.find_element(By.XPATH, "//input[@name='search']")
if input_search.is_displayed():
    actions.send_keys_to_element(input_search, "Proton radius puzzle").pause(5).\
        send_keys_to_element(input_search, "\n").pause(5).perform()

driver.quit()
