import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

GITHUB_URL = "https://github.com/ax-va/Selenium4-Raghavendra-2021"

FIREFOX_BIN_LOCATION = None
GECKODRIVER_LOCATION = None
CHROMEDRIVER_LOCATION = None

# Choose locations for different OS
if sys.platform == "win32":
    FIREFOX_BIN_LOCATION = "C:/Program Files/Mozilla Firefox/firefox.exe"
    GECKODRIVER_LOCATION = "../webdrivers/geckodriver-win32-0_32_0/geckodriver.exe"
    CHROMEDRIVER_LOCATION = "../webdrivers/chromedriver-win32-109_0_5414_74/chromedriver.exe"
elif sys.platform == "linux":
    FIREFOX_BIN_LOCATION = "/snap/firefox/current/usr/lib/firefox/firefox"
    GECKODRIVER_LOCATION = "/snap/firefox/current/usr/lib/firefox/geckodriver"
    CHROMEDRIVER_LOCATION = "../webdrivers/chromedriver-linux64-110_0_5481/chromedriver"
else:
    raise NotImplementedError("locations missing")

# Open Firefox browser
# Set executable binary Firefox location
options_firefox = webdriver.FirefoxOptions()
options_firefox.binary_location = FIREFOX_BIN_LOCATION
# Set webdriver location
service_firefox = FirefoxService(executable_path=GECKODRIVER_LOCATION)
driver_firefox = webdriver.Firefox(options=options_firefox, service=service_firefox)
# Open in browser
driver_firefox.get(GITHUB_URL)

# Open Chrome browser
# Set webdriver location
service_chrome = ChromeService(executable_path=CHROMEDRIVER_LOCATION)
driver_chrome = webdriver.Chrome(service=service_chrome)
# Open in browser
driver_chrome.get(GITHUB_URL)

time.sleep(5)

# Close Firefox browser
driver_firefox.close()
# Close Chrome browser
driver_chrome.close()
# Terminate the process for the driver
driver_firefox.quit()
# Terminate the process for the driver
driver_chrome.quit()

