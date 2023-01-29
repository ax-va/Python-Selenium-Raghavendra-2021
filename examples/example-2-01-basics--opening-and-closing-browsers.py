import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

MY_GITHUB_LINK = "https://github.com/ax-va/Web-Tests-Selenium4-Raghavendra-2021"

FIREFOX_PATH = None
GECKODRIVER_PATH = None
CHROMEDRIVER_PATH = None

if sys.platform == "win32":
    FIREFOX_PATH = "C:/Program Files/Mozilla Firefox/firefox.exe"
    GECKODRIVER_PATH = "../drivers/geckodriver-v0.32.0-win32/geckodriver.exe"
    CHROMEDRIVER_PATH = "../drivers/chromedriver-v109.0.5414.74-win32/chromedriver.exe"

# Open Mozilla Firefox browser on Windows
options_firefox = Options()
options_firefox.binary_location = FIREFOX_PATH
service_firefox = Service(executable_path=GECKODRIVER_PATH)
driver_firefox = webdriver.Firefox(options=options_firefox, service=service_firefox)
# Open in browser
driver_firefox.get(MY_GITHUB_LINK)

# Open Chrome browser on Windows
service_chrome = Service(executable_path=CHROMEDRIVER_PATH)
driver_chrome = webdriver.Chrome(service=service_chrome)
# Open in browser
driver_chrome.get(MY_GITHUB_LINK)

time.sleep(5)

# Close Firefox browser
driver_firefox.close()
# Close Chrome browser
driver_chrome.close()

