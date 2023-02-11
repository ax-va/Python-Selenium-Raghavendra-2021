import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

BROWSERS = ["chrome", "firefox"]
FIREFOX_WIN_BIN_LOCATION = "C:/Program Files/Mozilla Firefox/firefox.exe"
FIREFOX_LINUX_BIN_LOCATION = "/snap/firefox/current/usr/lib/firefox/firefox"
GECKODRIVER_WIN32_LOCATION = "../webdrivers/geckodriver-win32-0_32_0/geckodriver.exe"
GECKODRIVER_LINUS64_LOCATION = "/snap/firefox/current/usr/lib/firefox/geckodriver"
CHROMEDRIVER_WIN32_LOCATION = "../webdrivers/chromedriver-win32-109_0_5414_74/chromedriver.exe"
CHROME_DRIVER_LINUX64_LOCATION = "../webdrivers/chromedriver-linux64-110_0_5481/chromedriver"


def get_webdriver(browser=BROWSERS[0]):
    if browser not in BROWSERS:
        raise NotImplementedError("not implemented for " + browser)

    # Choose locations for different OS
    if sys.platform == "win32":
        firefox_bin_location = FIREFOX_WIN_BIN_LOCATION
        geckodriver_location = GECKODRIVER_WIN32_LOCATION
        chromedriver_location = CHROMEDRIVER_WIN32_LOCATION
    elif sys.platform == "linux":
        firefox_bin_location = FIREFOX_LINUX_BIN_LOCATION
        geckodriver_location = GECKODRIVER_LINUS64_LOCATION
        chromedriver_location = CHROME_DRIVER_LINUX64_LOCATION
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


def get_firefox_webdriver():
    return get_webdriver(browser="firefox")


def get_chrome_webdriver():
    return get_webdriver(browser="chrome")

