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
GOOGLE_URL = "https://google.com"

driver = webdrivers.get_chromedriver()
# Open my GitHub URL
driver.get(GITHUB_URL)
time.sleep(5)
# Open Google URL
driver.get(GOOGLE_URL)
time.sleep(5)
# Go back to previous page
driver.back()
time.sleep(5)
# Go forward
driver.forward()
time.sleep(5)
# Refresh page
driver.refresh()
time.sleep(5)
# Closes all the open windows and terminate the process for the driver
driver.quit()
