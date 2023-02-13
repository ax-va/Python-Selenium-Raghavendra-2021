import os
import pathlib
import sys
import time

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers


GITHUB_URL = "https://github.com/ax-va/Selenium4-Raghavendra-2021"

driver = webdrivers.get_chromedriver()
# Open URL page
driver.get(GITHUB_URL)
time.sleep(5)
# Open FILE page
website_abspath = os.path.abspath("../websites/website/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)
driver.quit()
