import os
import pathlib
import sys
import time

from selenium.webdriver import ActionChains
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
        <title>Buttons</title>
    </head>
    <body>
        <button id="default_btn" class="default" name="dft_btn" style="font-size:21px;">Default Button</button>
        <h1> Employee Form</h1>
        <form>
            Employee Name:
            <input type="text" id="ename" name="ename"><br><br>
            Employee Dept:
            <input type="text" id="dept" name="dept"><br><br>
            <input type="submit" value="Submit Button">
        </form>
    </body>
</html>
"""

with open("../webpages/buttons/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
actions = ActionChains(driver)
website_abspath = os.path.abspath("../webpages/buttons/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

default_button = driver.find_element(By.ID, "default_btn")
submit_button = driver.find_element(By.XPATH, "//*[@type='submit']")

assert default_button.is_displayed() is True  # correct
assert submit_button.is_displayed() is True  # correct
assert default_button.is_enabled() is True  # correct
assert submit_button.is_enabled() is True  # correct

# click 1
default_button.click()  # returns None
time.sleep(5)
# click 2
driver.find_element(By.ID, "default_btn").click()  # returns None
time.sleep(5)
# click 3
actions.move_to_element(default_button).pause(5).click().pause(5).perform()

default_button = driver.find_element(By.XPATH, "//button[text()='Default Button']")
# click 4
default_button.click()  # returns None
time.sleep(5)

default_button = driver.find_element(By.NAME, "dft_btn")
# click 5
default_button.click()  # returns None
time.sleep(5)

driver.quit()
