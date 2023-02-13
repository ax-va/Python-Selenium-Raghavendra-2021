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


GITHUB_URL = "https://github.com/ax-va/Selenium4-Raghavendra-2021"

driver = webdrivers.get_chromedriver()
# Open URL page
driver.get(GITHUB_URL)
time.sleep(5)
# Maximize window
driver.maximize_window()
time.sleep(5)
# Set full screen
driver.fullscreen_window()
time.sleep(5)
# Set window size
driver.set_window_size(width=600, height=800)
time.sleep(5)
# Set window position
driver.set_window_position(x=100, y=100)
time.sleep(5)
# Set window size with co-ordinates
driver.set_window_rect(x=50, y=50, width=800, height=600)
time.sleep(5)
# Get window position
window_position = driver.get_window_position()
print(window_position)  # {'x': 52, 'y': 50}
# Get window size
window_size = driver.get_window_size()
print(window_size)  # {'width': 800, 'height': 600}
