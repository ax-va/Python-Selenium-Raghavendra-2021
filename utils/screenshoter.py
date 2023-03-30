import os
from datetime import datetime


class Screenshoter:
    def __init__(self, driver, screenshots_dir, prefix="screenshot-"):
        self._driver = driver
        self._screenshots_dir = screenshots_dir
        self._prefix= prefix
        self._counter = 0

    @property
    def total(self):
        return self._counter

    def take_screenshot(self, description=""):
        prefix_timestamped = self._prefix + datetime.now().strftime("date-%y-%m-%d-time-%H-%M-%S-%f")
        file_name = prefix_timestamped if not description else prefix_timestamped + "-" + description
        file_path = os.path.join(self._screenshots_dir, file_name + ".png")
        self._driver.save_screenshot(file_path)
        self._counter += 1
