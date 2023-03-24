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
from utils.highlighter import Highlighter


HTML_CODE = """
<!DOCTYPE html>
<html>
    <body>
        <form id="EmployeeForm">
            <input name="fname" type="text" value="First Name"/>
            <br/>
            <input name="lname" type="text" value="Last Name"/>
            <br/>
            <input name="email" type="email" value="Email"/>
            <br/>
            <input name="password" type="password" value="Password"/>
            <br/>
            <input name="location" type="text" value="Location"/>
            <br/>
            <input name="next" type="submit" value="Login"/>
            <input name="next" type="button" value="Clear"/>
            <button type="button">Submit</button>
        </form>
    </body>
</html>
"""

with open("../webpages/employee-form/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
highlighter = Highlighter(driver)
website_abspath = os.path.abspath("../webpages/employee-form/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# find_element(...) returns a first matched element by a given locator, otherwise it throws an exception.
# find_elements(...) returns all matched elements in a list by a given locator.
# If there are no such elements, the list is empty.

form_employee = driver.find_element(By.ID, "EmployeeForm")
highlighter.highlight_and_wait(form_employee)

driver.quit()
