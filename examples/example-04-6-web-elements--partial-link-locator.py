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
        <title>Title</title>
    </head>
    <body>
        <div class="container">Categories
            <a href="python.html">Python</a>
            <a href="web.html">Web Development</a>
            <a href="machine.html">Machine Learning</a>
            <a href="databases.html">Database</a>
        </div>
    </body>
</html>
"""

with open("../webpages/categories-links/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
highlighter = Highlighter(driver)
website_abspath = os.path.abspath("../webpages/categories-links/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# Locate elements using partial link text
anchor1 = driver.find_element(By.PARTIAL_LINK_TEXT, "Py")
highlighter.highlight_and_wait(anchor1)
anchor2 = driver.find_element(By.PARTIAL_LINK_TEXT, "taba")
highlighter.highlight_and_wait(anchor2)

# anchor3 = driver.find_element(By.LINK_TEXT, "py")
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: ...
# anchor4 = driver.find_element(By.LINK_TEXT, "taBa")
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: ...

driver.quit()
