"""
Selenium has bugs with drag-and-drop and action chains:
1) It does not work in Chrome and Firefox on Windows;
2) Positions are determined not correctly in Chrome and Firefox on Ubuntu;
3) release() does not work in Chrome and Firefox on Ubuntu.
"""
import os
import pathlib
import sys
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers

HTML_CODE = """
<!DOCTYPE HTML>
<html>
    <head>
        <style type="text/css">
            #myTarget {
              width: 100px;
              height: 100px;
              padding: 10px;
              border: 1px solid #aaaaaa;
            }
        </style>
        <script type="text/javascript">
            function dragOver(ev) {
              ev.preventDefault();
            }

            function drag(ev) {
              ev.dataTransfer.setData("text", ev.target.id);
            }

            function drop(ev) {
              ev.preventDefault();
              var data = ev.dataTransfer.getData("text");
              ev.target.appendChild(document.getElementById(data));
            }
        </script>
    </head>
    <body>
        <p>Drag the image into the rectangle:</p>
        <div id="myTarget" ondrop="drop(event)" ondragover="dragOver(event)"></div>
        <br/>
        <img id="mySource" src="img.png" draggable="true" ondragstart="drag(event)" width="100" height="100"/>
    </body>
</html>
"""

with open("../webpages/drag-and-drop/drag-and-drop.html", "w") as f:
    f.write(HTML_CODE)

website_abspath = os.path.abspath("../webpages/drag-and-drop/drag-and-drop.html")
driver = webdrivers.get_chromedriver()
actions = ActionChains(driver)
driver.get("file:///" + website_abspath)
time.sleep(5)

my_source = driver.find_element(By.ID, "mySource")
my_target = driver.find_element(By.ID, "myTarget")

actions.drag_and_drop(my_source, my_target).pause(5).perform()
# actions.click_and_hold(my_source).move_to_element(my_target).pause(5).release().pause(5).perform()
# offset_x = my_target.location["x"]
# offset_y = my_target.location["y"]
# actions.click_and_hold(my_source).move_by_offset(offset_x, offset_y).pause(5).release().pause(5).perform()
driver.quit()

driver = webdrivers.get_chromedriver()
actions = ActionChains(driver)
driver.get("file:///" + website_abspath)
time.sleep(5)

my_source = driver.find_element(By.ID, "mySource")
my_target = driver.find_element(By.ID, "myTarget")

actions.drag_and_drop_by_offset(my_source, my_target.location["x"], my_target.location["y"]).pause(5).perform()

# Closes all the open windows and terminate the process for the driver
driver.quit()
