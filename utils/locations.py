"""
Hardcoded browser and webdriver locations in a dictionary
"""

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
