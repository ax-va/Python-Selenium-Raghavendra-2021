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
for index, anchor in enumerate(anchors[:15]):
    url = anchor.get_attribute('href')
    response = requests.head(url)
    print(f"{index} \tStatus code of requesting {url} received: {response.status_code}")
# Checking for href URLs:
# 0 	Status code of requesting https://en.wikipedia.org/wiki/Vacuum_polarization#bodyContent received: 200
# 1 	Status code of requesting https://en.wikipedia.org/wiki/Main_Page received: 200
# 2 	Status code of requesting https://en.wikipedia.org/wiki/Special:Search received: 200
# 3 	Status code of requesting https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Vacuum+polarization received: 200
# 4 	Status code of requesting https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Vacuum+polarization received: 200
# 5 	Status code of requesting https://en.wikipedia.org/w/index.php?title=Special:CreateAccount&returnto=Vacuum+polarization received: 200
# 6 	Status code of requesting https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Vacuum+polarization received: 200
# 7 	Status code of requesting https://en.wikipedia.org/wiki/Help:Introduction received: 200
# 8 	Status code of requesting https://en.wikipedia.org/wiki/Special:MyContributions received: 200
# 9 	Status code of requesting https://en.wikipedia.org/wiki/Special:MyTalk received: 200
# 10 	Status code of requesting https://en.wikipedia.org/wiki/Main_Page received: 200
# 11 	Status code of requesting https://en.wikipedia.org/wiki/Wikipedia:Contents received: 200
# 12 	Status code of requesting https://en.wikipedia.org/wiki/Portal:Current_events received: 200
# 13 	Status code of requesting https://en.wikipedia.org/wiki/Special:Random received: 302
# 14 	Status code of requesting https://en.wikipedia.org/wiki/Wikipedia:About received: 200

images = driver.find_elements(By.CSS_SELECTOR, "img")
print("Checking for image URLs:")
for index, image in enumerate(images[:15]):
    url = image.get_attribute('src')
    response = requests.head(url)
    print(f"{index} \tStatus code of requesting {url} received: {response.status_code}")
# Checking for image URLs:
# 0 	Status code of requesting https://en.wikipedia.org/static/images/icons/wikipedia.png received: 200
# 1 	Status code of requesting https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-wordmark-en.svg received: 200
# 2 	Status code of requesting https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-tagline-en.svg received: 200
# 3 	Status code of requesting https://upload.wikimedia.org/wikipedia/foundation/2/20/CloseWindow19x19.png received: 200
# 4 	Status code of requesting https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Vacuum_polarization.svg/144px-Vacuum_polarization.svg.png received: 200
# 5 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/9d4acf672f3a6e13571d0302c9600d3ad38ebb94 received: 200
# 6 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/555d3ceb1a992c06879fcf8435c61d9ff5915653 received: 200
# 7 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/b79333175c8b3f0840bfb4ec41b8072c83ea88d3 received: 200
# 8 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/86ebe5b7bdbef2ecd7cf34859c5c643a96cd4185 received: 200
# 9 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/f50e974e9e087a97e8036dc65adbe8ef3a097357 received: 200
# 10 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/06809d64fa7c817ffc7e323f85997f783dbdf71d received: 200
# 11 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/453f9f3238a64a30870504c3eb9e39861a0f7fc1 received: 200
# 12 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/71a8fe7fb4923d0344a5e464c47d62c3b1c454d9 received: 200
# 13 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/b79333175c8b3f0840bfb4ec41b8072c83ea88d3 received: 200
# 14 	Status code of requesting https://wikimedia.org/api/rest_v1/media/math/render/svg/20787b696b880d088ce7ae95428712d9cd9386fc received: 200

"""
HTTP Code     Description
200           Valid Link
302           URL Redirection
400           Bad Request
401           Unauthorized
404           Link/Page not Found
500           Internal Error
"""

driver.quit()
