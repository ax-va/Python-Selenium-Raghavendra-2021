import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Open web Chrome browser using webdriver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# Add URL to open in browser
driver.get("http://www.google.com")
try:
    # Find element of button "Reject all"
    button_reject_all = driver.find_element(By.ID, "W0wltc")
    # Click button
    button_reject_all.click()
except Exception:
    pass
# Get element of search bar
search = driver.find_element(By.NAME, "q")
# Write text to search
search.send_keys("github ax-va")
# Wait 5 seconds
time.sleep(5)
# Submit text to search bar
search.submit()
# Wait 5 seconds
time.sleep(5)
# Get first item
first_item = driver.find_element(By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
# Click first item
first_item.click()
# Wait 5 seconds
time.sleep(5)
# Close Chrome browser
driver.quit()
