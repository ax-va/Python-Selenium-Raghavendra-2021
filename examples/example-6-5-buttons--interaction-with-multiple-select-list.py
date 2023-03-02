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
        <title>Multiple Select List</title>
    </head>
    <body>
        <h1>Fruit Salad</h1>
        <label for="fruits">Choose Multiple Fruits:</label>
        <select id="fruits" name="fruits" size="7" multiple>
            <option value="apple">Apple</option>
            <option value="banana">Banana</option>
            <option value="cranberry">Cranberry</option>
            <option value="dragonfruit">Dragon Fruit</option>
            <option value="elderberry">Elderberry</option>
            <option value="figs">Figs Fruit</option>
            <option value="grapes">Grapes</option>
        </select>
        <br/>
        <p>For Windows and Linux, hold the Ctrl button while selecting options. 
        For MacOS, hold the Command button while selecting options.</p>
    </body>
</html>
"""

with open("../webpages/multiple-select-list/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
website_abspath = os.path.abspath("../webpages/multiple-select-list/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# Use the Select class
multiple_select_list = Select(driver.find_element(By.ID, "fruits"))
# Select options
multiple_select_list.select_by_index(0)
time.sleep(5)
multiple_select_list.select_by_value("cranberry")
time.sleep(5)
multiple_select_list.select_by_visible_text("Elderberry")
time.sleep(5)
multiple_select_list.select_by_index(6)
time.sleep(5)
# Deselect an option only in multi-select
multiple_select_list.deselect_by_index(6)
time.sleep(5)
multiple_select_list.deselect_by_value("cranberry")
time.sleep(5)
multiple_select_list.deselect_by_visible_text("Elderberry")
time.sleep(5)

# Verify the first selected option
assert multiple_select_list.first_selected_option.get_attribute("value") == "apple"

multiple_select_list.deselect_by_value("apple")
time.sleep(5)
multiple_select_list.select_by_value("elderberry")
time.sleep(5)
multiple_select_list.select_by_value("apple")
time.sleep(5)

# Verify the first selected option
assert multiple_select_list.first_selected_option.get_attribute("value") == "apple"

# Get all selected options
for selected_option in multiple_select_list.all_selected_options:
    print(selected_option.text)
# Apple
# Elderberry

# Deselect all options
multiple_select_list.deselect_all()
time.sleep(5)

# Verify if there are no selected options (the list of selected options is empty)
assert not multiple_select_list.all_selected_options

driver.quit()
