import os
import pathlib
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as e_cs
from selenium.webdriver.support.wait import WebDriverWait

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
        <title>Inline Frames (IFrames)</title>
    </head>
    <body>
        <div>
            <h5>IFrame0</h5>
            <iframe id="iframe0" name="apress" src="https://www.apress.com" height="600" width="600"></iframe>
        </div>
        <div>
            <h5>IFrame1</h5>
            <iframe id="iframe1" name="wiki" src="https://www.wikipedia.org" height="600" width="600"></iframe>
        </div>
    </body>
</html>
"""

with open("../webpages/iframes/index.html", "w") as f:
    f.write(HTML_CODE)

driver = webdrivers.get_chromedriver()
website_abspath = os.path.abspath("../webpages/iframes/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)

# Switch to the frame with name
driver.switch_to.frame("apress")
# Switch to the main (most parent) frame
driver.switch_to.default_content()

# Switch to the frame with name
driver.switch_to.frame("wiki")
# Switch to the parent frame
driver.switch_to.parent_frame()

# Switch to the frame with name
driver.switch_to.frame("wiki")
# Switch to the parent frame
driver.switch_to.parent_frame()

# Switch to the frame with id
driver.switch_to.frame("iframe0")
# Switch to the parent frame
driver.switch_to.parent_frame()

# Switch to the frame with id
driver.switch_to.frame("iframe1")
# Switch to the parent frame
driver.switch_to.parent_frame()

# Switch to frame 0
driver.switch_to.frame(0)
# Switch to the parent frame
driver.switch_to.parent_frame()

# Switch to frame 1
driver.switch_to.frame(1)
# Switch to the parent frame
driver.switch_to.parent_frame()

# Switch to frame with WebElement
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='https://www.apress.com']"))
# Switch to the parent frame
driver.switch_to.parent_frame()

# Switch to frame with WebElement
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='https://www.wikipedia.org']"))
# Switch to the parent frame
driver.switch_to.parent_frame()

driver.get("file:///" + website_abspath)
WebDriverWait(driver, 5).until(e_cs.frame_to_be_available_and_switch_to_it("apress"))

driver.get("file:///" + website_abspath)
WebDriverWait(driver, 5).until(e_cs.frame_to_be_available_and_switch_to_it("iframe0"))

driver.get("file:///" + website_abspath)
WebDriverWait(driver, 5).until(
    e_cs.frame_to_be_available_and_switch_to_it(
        driver.find_element(By.XPATH, "//iframe[@src='https://www.apress.com']")
    )
)

driver.get("file:///" + website_abspath)
WebDriverWait(driver, 5).until(
    e_cs.frame_to_be_available_and_switch_to_it(
        driver.find_element(By.CSS_SELECTOR, "iframe:nth-of-type(1)")
    )
)

driver.quit()
