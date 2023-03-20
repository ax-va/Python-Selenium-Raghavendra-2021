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
        <title>Textboxes</title>
    </head>
    <body>
        <h1>Single Line Textbox</h1>
        <label for="book1">Book Name:</label>
        <input type="text" id="book1" name="book">
        <h1>Textarea</h1>
        <label for="book2">Book Name:</label>
        <br/>
        <textarea id="book2" cols="50" rows="5"></textarea>
    </body>
</html>
"""

with open("../webpages/textboxes/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
website_abspath = os.path.abspath("../webpages/textboxes/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# Input text to textboxes
input_book_name = driver.find_element(By.ID, "book1")
input_book_name.send_keys("Selenium")
time.sleep(5)

textarea_book_name = driver.find_element(By.ID, "book2")
textarea_book_name.send_keys("Selenium Selenium \n Selenium")
time.sleep(5)

# Get textboxes' values
input_book_name_value = input_book_name.get_property("value")
assert input_book_name_value == "Selenium"

textarea_book_name_value = textarea_book_name.get_property("value")
assert textarea_book_name_value == "Selenium Selenium \n Selenium"

driver.quit()
