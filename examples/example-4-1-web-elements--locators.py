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


website_abspath = os.path.abspath("../webpages/employee-form/index.html")
driver = webdrivers.get_chromedriver()
highlighter = Highlighter(driver)
driver.get("file:///" + website_abspath)
time.sleep(5)

form_employee = driver.find_element(By.ID, "EmployeeForm")
highlighter.highlight_and_wait(form_employee)

input_fname = driver.find_element(By.NAME, "fname")
highlighter.highlight_and_wait(input_fname)

input_email = driver.find_element(By.NAME, "email")
highlighter.highlight_and_wait(input_email)

# If multiple elements have the same attribute, then the first matched is returned
input_next = driver.find_element(By.NAME, "next")
highlighter.highlight_and_wait(input_next)

input_location = driver.find_element(By.XPATH, "/html/body/form/input[5]")
highlighter.highlight_and_wait(input_location)

input_lname = driver.find_element(By.XPATH, "//form/input[2]")
highlighter.highlight_and_wait(input_lname)

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

driver.get("file:///" + website_abspath)
time.sleep(5)

form_employee = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm")
highlighter.highlight_and_wait(form_employee)

input_first = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm input")
highlighter.highlight_and_wait(input_first)

# Find element if:
# it is the 2nd "input" child of the parent
input_second = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm input:nth-of-type(2)")  # the same element as below
highlighter.highlight_and_wait(input_second)

# Find element if:
# 1) it is an "input" element;
# 2) it is the 3rd child of the parent
input_second = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm input:nth-child(3)")  # the same element as above
# Highlight with another color
highlighter.highlight_and_wait(input_second, background="peachpuff")

button_submit = driver.find_element(By.CSS_SELECTOR, "#EmployeeForm *:last-child")
highlighter.highlight_and_wait(button_submit)

driver.quit()
