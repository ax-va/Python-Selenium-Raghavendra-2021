import os
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


HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Radio Buttons</title>
    </head>
    <body>
        <h3>Select your gender:</h3>
            <div>
                <input type="radio" id="male" name="gender" value="g1" checked>
                <label for="male">Male</label>
            </div>
            <div>
                <input type="radio" id="female" name="gender" value="g2">
                <label for="female">Female</label>
            </div>
            <div>
                <input type="radio" id="other" name="gender" value="g3">
                <label for="other">Diverse</label>
            </div>
    </body>
</html>
"""

with open("../webpages/radio-buttons/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
website_abspath = os.path.abspath("../webpages/radio-buttons/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# Select 'diverse' radio button
radio_button_other = driver.find_element(By.ID, "other")
radio_button_other.click()
time.sleep(5)

radio_button_female = driver.find_element(By.ID, "female")
radio_button_female.click()
time.sleep(5)

assert radio_button_female.get_attribute("type") == "radio"  # correct
assert radio_button_other.get_attribute("type") == "radio"  # correct
assert radio_button_female.is_selected() is True  # correct
assert radio_button_female.get_attribute("checked") == "true"  # correct
assert radio_button_other.is_selected() is False  # correct
assert radio_button_other.get_attribute("checked") != "true"  # correct
assert radio_button_other.get_attribute("checked") is None  # correct

driver.quit()
