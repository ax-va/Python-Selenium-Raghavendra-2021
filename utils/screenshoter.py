import os
from datetime import datetime


class Screenshoter:
    def __init__(self, driver, screenshots_dir, head_name="screenshot-"):
        self._driver = driver
        self._screenshots_dir = screenshots_dir
        self._head_name = head_name
        self._counter = 1

    @property
    def counted(self):
        return self._counter

    def take_screenshot(self, description=""):
        head_name_timestamped = self._head_name + datetime.now().strftime("date-%y-%m-%d-time-%H-%M-%S-%f")
        file_name = head_name_timestamped if not description else head_name_timestamped + "-" + description
        file = file_name + ".png"
        file_path = os.path.join(self._screenshots_dir, file)
        self._driver.save_screenshot(file_path)
        self._counter += 1
