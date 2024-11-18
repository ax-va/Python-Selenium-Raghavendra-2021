import os
import pathlib
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
        <title>Select List</title>
    </head>
    <body>
        <h1>Blood Group</h1>
        <label for="bld_grp">Choose Blood Group:</label>
        <select id="bld_grp" name="blood">
            <option value="A">A type</option>
            <option value="B">B type</option>
            <option value="O">O type</option>
            <option value="AB">AB type</option>
        </select>
    </body>
</html>
"""

with open("../webpages/select-list/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
website_abspath = os.path.abspath("../webpages/select-list/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

options = driver.find_elements(By.TAG_NAME, "option")
for option in options:
    print("Option:", option.get_attribute("value"))
# Option: A
# Option: B
# Option: O
# Option: AB

# Use the Select class
select_list = Select(driver.find_element(By.ID, "bld_grp"))
# Select options
select_list.select_by_visible_text("O type")
time.sleep(5)
select_list.select_by_value("B")
time.sleep(5)
select_list.select_by_index("0")
time.sleep(5)
select_list.select_by_index(0)
time.sleep(5)
# Select the last option
select_list.select_by_index(len(select_list.options)-1)
time.sleep(5)

# Verify if selected
assert select_list.first_selected_option.get_attribute("value") == "AB"

# Get all selected options
for selected_option in select_list.all_selected_options:
    print(selected_option.text)
# AB type

# Get all options
for option in select_list.options:
    print(option.text)
# A type
# B type
# O type
# AB type

driver.quit()