import os


class ScreenshotMaker:
    def __init__(self, driver, screenshot_dir, count_from=1):
        self._driver = driver
        self._screenshot_dir = screenshot_dir
        self._counter = count_from

    def make_screenshot(self, screenshot_name=""):
        counter_name = f"screenshot-{self._counter}"
        file_name = counter_name if not screenshot_name else counter_name + f"-{screenshot_name}"
        file = file_name + ".png"
        file_path = os.path.join(self._screenshot_dir, file)
        self._driver.save_screenshot(file_path)
        self._counter += 1

