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
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Apress</title>
    </head>
    <body>
        <p class="press">Apress Publication</p>
        <!--HTML tag with multiple CSS classes-->
        <p class="my-class text-justify">New York</p>
        <p id="apress_press">Apress press</p>
        <p id="apress_123">Apress 123</p>
        <p id="123_apress_press">123 Apress press</p>
        <p class ="container" id="apress" style="align-self:center;">Some more text</p>
        <h1>Python with Selenium</h1>
    </body>
</html>
"""

with open("../webpages/apress/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
highlighter = Highlighter(driver)
website_abspath = os.path.abspath("../webpages/apress/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# CSS selector is used
class1 = driver.find_element(By.CLASS_NAME, "press")
highlighter.highlight_and_wait(class1)
class2 = driver.find_element(By.CLASS_NAME, "my-class")
highlighter.highlight_and_wait(class2)
class2 = driver.find_element(By.CLASS_NAME, "text-justify")
highlighter.highlight_and_wait(class2)
class3 = driver.find_element(By.CLASS_NAME, "my-class.text-justify")
highlighter.highlight_and_wait(class3)

driver.quit()
