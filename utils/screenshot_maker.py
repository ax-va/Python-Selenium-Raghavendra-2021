import os
from datetime import datetime


class ScreenshotMaker:
    def __init__(self, driver, screenshots_dir):
        self._driver = driver
        self._screenshots_dir = screenshots_dir

    def make_screenshot(self, description=""):
        header_name = "screenshot-" + datetime.now().strftime("date-%y-%m-%d-time-%H-%M-%S-%f")
        file_name = header_name if not description else header_name + "-" + description
        file = file_name + ".png"
        file_path = os.path.join(self._screenshots_dir, file)
        self._driver.save_screenshot(file_path)
