import logging
import time

from selenium.common import JavascriptException


class Highlighter:
    def __init__(self, webdriver, wait_in_sec=5):
        self._webdriver = webdriver
        self._wait_in_sec = wait_in_sec
        self._background_color = "darkseagreen"
        self._border_color = "lightgreen"

    @property
    def webdriver(self):
        return self._webdriver

    @webdriver.setter
    def webdriver(self, value):
        self._webdriver = value

    @property
    def wait_in_sec(self):
        return self._wait_in_sec

    @wait_in_sec.setter
    def wait_in_sec(self, value):
        self._wait_in_sec = value

    def highlight_element(self, element, background_color=None, border_color=None):
        bg_color = self._background_color if background_color is None else background_color
        b_color = self._border_color if border_color is None else border_color

        try:
            self._webdriver.execute_script(
                f"arguments[0].setAttribute('style', 'background: {bg_color}; border: 2px solid {b_color};');",
                element
            )
        except JavascriptException as e:
            logging.warning(str(e))

    def highlight_element_and_wait(self, element, background_color=None, border_color=None):
        self.highlight_element(element, background_color, border_color)
        time.sleep(self._wait_in_sec)
