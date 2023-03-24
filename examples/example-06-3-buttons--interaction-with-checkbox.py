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
        <title>Checkbox</title>
    </head>
    <body>
        <h3>Browsers:</h3>
        <form>
            <input type="checkbox" id="firefox" name="browser" value="b1" checked/>
            <label for="firefox">Firefox</label>
            <br/>
            <input type="checkbox" id="chrome" name="browser" value="b2"/>
            <label for="chrome">Chrome</label>
            <br/>
            <input type="checkbox" id="opera" name="browser" value="b3"/>
            <label for="opera">Opera</label>
            <br/>
            <input type="checkbox" id="edge" name="browser" value="b4"/>
            <label for="edge">Edge</label>
            <br/>
        </form>
    </body>
</html>
"""

with open("../webpages/checkbox/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
website_abspath = os.path.abspath("../webpages/checkbox/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# Select Opera check button
driver.find_element(By.ID, "opera").click()
time.sleep(5)

assert driver.find_element(By.ID, "chrome").get_attribute("type") == "checkbox"  # correct
assert driver.find_element(By.ID, "firefox").is_selected() is True  # correct
assert driver.find_element(By.ID, "firefox").get_attribute("checked") == "true" # correct
assert driver.find_element(By.ID, "chrome").is_selected() is False  # correct
assert driver.find_element(By.ID, "chrome").get_attribute("checked") is None  # correct
assert driver.find_element(By.ID, "opera").is_selected() is True  # correct
assert driver.find_element(By.ID, "opera").get_attribute("checked") == "true"  # correct

# Unselect check buttons
driver.find_element(By.ID, "firefox").click()
time.sleep(5)
driver.find_element(By.ID, "opera").click()
time.sleep(5)

assert driver.find_element(By.ID, "firefox").is_selected() is False  # correct
assert driver.find_element(By.ID, "firefox").get_attribute("checked") is None  # correct

driver.quit()
