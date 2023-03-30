import os
from datetime import datetime


class ScreenshotMaker:
    def __init__(self, driver, screenshot_dir):
        self._driver = driver
        self._screenshot_dir = screenshot_dir

    def make_screenshot(self, screenshot_name=""):
        header_name = "screenshot-" + datetime.now().strftime("date-%y-%m-%d-time-%H-%M-%S-%f")
        file_name = header_name if not screenshot_name else header_name + f"-{screenshot_name}"
        file = file_name + ".png"
        file_path = os.path.join(self._screenshot_dir, file)
        self._driver.save_screenshot(file_path)
