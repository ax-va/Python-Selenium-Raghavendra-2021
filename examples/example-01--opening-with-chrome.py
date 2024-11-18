import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Open web Chrome browser using webdriver
driver = webdriver.Chrome(
    service=ChromeService(
        ChromeDriverManager().install()
    )
)

# Add URL to open in browser
driver.get("http://www.google.com")

try:
    # Find element of button "Reject all"
    button_reject_all = driver.find_element(By.ID, "W0wltc")
except NoSuchElementException:
    pass
else:
    # Click button "Reject all"
    button_reject_all.click()

# Get element of search bar
search_bar = driver.find_element(By.NAME, "q")

# Write text to search
search_bar.send_keys("github ax-va")

# Wait 5 seconds
time.sleep(5)

# Submit text to search bar
search_bar.submit()

# Wait 5 seconds
time.sleep(5)

# Get first found item
results_item = driver.find_element(By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")

# Click first found item
results_item.click()

# Wait 5 seconds
time.sleep(5)

# Close Chrome browser
driver.quit()
