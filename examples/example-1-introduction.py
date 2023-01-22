import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Open web Chrome browser using webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Add URL to open in browser
driver.get("http://www.google.com")
# Find Element of button "Reject all"
button_reject_all = driver.find_element(By.XPATH, "(//button)[4]")
# Click button
button_reject_all.click()
# Find Element of search bar
search = driver.find_element(By.NAME, "q")
# Write text
search.send_keys("github ax-va")
# Submit text to search bar
search.submit()
# Wait 5 seconds
time.sleep(5)
# Get first item
first_item = driver.find_element(By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
# Click
first_item.click()
# Wait 5 seconds
time.sleep(5)
# Close Chrome browser
driver.quit()
