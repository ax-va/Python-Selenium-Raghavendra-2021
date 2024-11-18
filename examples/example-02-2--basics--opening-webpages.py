import os
import pathlib
import sys
import time

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers
from webpages.urls import GITHUB_URL

driver = webdrivers.get_chromedriver()
# Open URL page
driver.get(GITHUB_URL)
time.sleep(5)

# Check if "Selenium" is in the webpage title
assert "Selenium" in driver.title

HTML_CODE = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Webpage</title>
</head>
    <body>
        This is <b><i>webpage</i></b>
        <h1>Font size</h1>
        <h2>Font size</h2>
        <h3>Font size</h3>
        <h4>Font size</h4>
        <h5>Font size</h5>
        <h6>Font size</h6>
    </body>
</html>
"""

with open("../webpages/webpage/index.html", "w") as f:
    f.write(HTML_CODE)

# Open FILE page
website_abspath = os.path.abspath("../webpages/webpage/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# Check the webpage title
assert driver.title == "Webpage"

# Closes all the open windows and terminate the process for the driver
driver.quit()
