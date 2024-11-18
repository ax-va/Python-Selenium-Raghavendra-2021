import pathlib
import sys

from io import BytesIO
from PIL import Image  # Pillow installed (by pip) that is a friendly fork of PIL, Python Imaging Library
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from webpages.urls import GOOGLE_URL


TIMEOUT = 10  # seconds
POLLING_EVERY = 0.1  # second

driver = webdrivers.get_chromedriver()
driver.get(GOOGLE_URL)

try:
    button_reject_all = driver.find_element(By.ID, "W0wltc")
    # Save screenshots to PNG.
    # Two methods are equivalent:
    driver.save_screenshot("../screenshots/s1-dialog_agreement1.png")
    driver.get_screenshot_as_file("../screenshots/s1-dialog_agreement2.png")
    # Save screenshots in multiple formats
    png_binary_data = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(png_binary_data))
    # Save to PNG
    image.save("../screenshots/s1-dialog_agreement3.png")
    # Save to JPEG
    image.convert("RGB").save("../screenshots/s1-dialog_agreement3.jpg")
except NoSuchElementException:
    pass
else:
    button_reject_all.click()

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("github ax-va")
# Save screenshot to PNG
driver.save_screenshot("../screenshots/s2-search_bar-with-request.png")
search_bar.submit()
# Save screenshot to PNG
driver.save_screenshot("../screenshots/s3-found-results.png")
results_item = driver.find_element(By.XPATH, "(//a//*[contains(text(), 'ax-va')])[1]")
results_item.click()
# Save screenshot to PNG
driver.save_screenshot("../screenshots/s4-github-page.png")

driver.quit()
