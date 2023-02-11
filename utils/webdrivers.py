import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

BROWSERS = ["chrome", "firefox"]
LOCATIONS = \
    {
        "win32":
            {
                "firefox":
                    {
                        "bin": "C:/Program Files/Mozilla Firefox/firefox.exe",
                        "webdriver": "../webdrivers/geckodriver-win32-0_32_0/geckodriver.exe",
                    },
                "chrome":
                    {
                        "webdriver": "../webdrivers/chromedriver-win32-109_0_5414_74/chromedriver.exe",
                    },
        "linux64":
            {
                "firefox":
                    {
                        "bin": "/snap/firefox/current/usr/lib/firefox/firefox",
                        "webdriver": "/snap/firefox/current/usr/lib/firefox/geckodriver",
                    },
                "chrome":
                    {
                        "webdriver": "../webdrivers/chromedriver-linux64-110_0_5481/chromedriver",
                    }
                }
            }
    }


def get_webdriver(browser=BROWSERS[0]):
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


def get_firefox_webdriver():
    return get_webdriver(browser="firefox")


def get_chrome_webdriver():
    return get_webdriver(browser="chrome")

