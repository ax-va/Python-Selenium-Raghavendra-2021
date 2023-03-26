import pathlib
import sys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from webpages.urls import GOOGLE_URL


TIMEOUT = 20  # seconds

driver = webdrivers.get_chromedriver()
driver.get(GOOGLE_URL)

try:
    # Find element of button "Reject all"
    button_reject_all = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "W0wltc")))
except TimeoutException:
    pass
else:
    # Click button "Reject all"
    button_reject_all.click()

try:
    # Try to find non-existent element.
    # Poll TIMEOUT seconds to find element with default polling every 0.5 second.
    non_existent = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "Non-existent")))
except TimeoutException:
    pass

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("github ax-va")
search_bar.submit()
results_item = driver.find_element(By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
results_item.click()

driver.quit()

# Commonly used expected conditions:
# - alert_is_present()
# - element_located_selection_state_to_be(ui_locator, is_selected)
# - element_located_to_be_selected(ui_locator)
# - element_selection_state_to_be(ui_element, is_selected)
# - element_to_be_clickable(ui_locator)
# - element_to_be_selected(ui_element)
# - frame_to_be_available_and_switch_to_it(ui_locator)
# - invisibility_of_element_located(ui_locator)
# - title_is(title)
# - staleness_of(ui_element)
# - text_to_be_present_in_element(ui_locator, inner_text)
# - text_to_be_present_in_element_value(ui_locator, value)
# - title_contains(title_text)
# - visibility_of(ui_element)
# - visibility_of_all_elements_located(ui_locator)
# - visibility_of_any_elements_located(ui_locator)
# - visibility_of_element_located(ui_locator)
# - invisibility_of_element_located(ui_locator)
# - new_window_is_opened(current_handles)
# - number_of_windows_to_be(num_windows)
# - url_changes(url)
# - url_contains(url)
# - url_matches(url)
# - url_to_be(url)
# - presence_of_all_elements_located(locator)
# - presence_of_element_located(locator)

# You can define custom wait conditions:
# https://selenium-python.readthedocs.io/waits.html

