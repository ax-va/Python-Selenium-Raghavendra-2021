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

input_fname = driver.find_element(By.XPATH, "//input[@name='fname' and @type='text']")
highlighter.highlight_and_wait(input_fname)

# list with two elements
form_elements = driver.find_elements(By.XPATH, "//input[@name='fname' or @name='lname']")
print(len(form_elements))  # 2

# list with three elements
form_elements = driver.find_elements(By.XPATH, "//input[@name='fname' or @name='lname' or @type='email']")
print(len(form_elements))  # 3

# list with one element
input_password_list = driver.find_elements(By.XPATH, "//input[contains(@name, 'pass')]")
highlighter.highlight_and_wait(input_password_list[0])
print(len(input_password_list))  # 1

button_submit = driver.find_element(By.XPATH, "//*[text()='Submit']")
highlighter.highlight_and_wait(button_submit)

form_employee = driver.find_element(By.XPATH, "//*[starts-with(@id, 'Employee')]")
highlighter.highlight_and_wait(form_employee)

driver.quit()
