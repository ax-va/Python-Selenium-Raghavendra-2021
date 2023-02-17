import json
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

# my modules
from utils.browsers import BROWSERS
from utils.locations import LOCATIONS


def get_webdriver(browser="chrome"):
    if browser not in BROWSERS:
        raise NotImplementedError("not implemented for " + browser)

    # Choose locations for different OS
    if sys.platform == "win32":
        firefox_bin_location = LOCATIONS["win32"]["firefox"]["bin"]
        geckodriver_location = LOCATIONS["win32"]["firefox"]["webdriver"]
        chromedriver_location = LOCATIONS["win32"]["chrome"]["webdriver"]
    elif sys.platform == "linux":
        firefox_bin_location = LOCATIONS["linux64"]["firefox"]["bin"]
        geckodriver_location = LOCATIONS["linux64"]["firefox"]["webdriver"]
        chromedriver_location = LOCATIONS["linux64"]["chrome"]["webdriver"]
    else:
        raise NotImplementedError("locations missing")

    if browser.lower() == "firefox":
        # Set executable binary Firefox location
        options_firefox = webdriver.FirefoxOptions()
        options_firefox.binary_location = firefox_bin_location
        # Set webdriver location
        service_firefox = FirefoxService(executable_path=geckodriver_location)
        driver_firefox = webdriver.Firefox(options=options_firefox, service=service_firefox)
        return driver_firefox
    elif browser.lower() == "chrome":
        # Set webdriver location
        service_chrome = ChromeService(executable_path=chromedriver_location)
        driver_chrome = webdriver.Chrome(service=service_chrome)
        return driver_chrome


def get_geckodriver():
    return get_webdriver(browser="firefox")


def get_chromedriver():
    return get_webdriver(browser="chrome")

