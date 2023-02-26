import requests
import pathlib
import sys
import time

from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from webpages.urls import WIKI_URL


driver = webdrivers.get_chromedriver()
driver.get(WIKI_URL)
time.sleep(5)

anchors = driver.find_elements(By.CSS_SELECTOR, "a")
print("Checking for href URLs:")
for index, anchor in enumerate(anchors[:20]):
    url = anchor.get_attribute('href')
    response = requests.head(url)
    print(f"{index} \tStatus code of requesting {url} received: {response.status_code}")

images = driver.find_elements(By.CSS_SELECTOR, "img")
print("Checking for image URLs:")
for index, image in enumerate(images[:20]):
    url = image.get_attribute('src')
    response = requests.head(url)
    print(f"{index} \tStatus code of requesting {url} received: {response.status_code}")

# HTTP Code     Description
# 200           Valid Link
# 302           URL Redirection
# 400           Bad Request
# 401           Unauthorized
# 404           Link/Page not Found
# 500           Internal Error

driver.quit()
