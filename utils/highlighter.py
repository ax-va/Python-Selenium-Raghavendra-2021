import logging
import time

from selenium.common import JavascriptException


class Highlighter:
    def __init__(self, webdriver, wait_in_sec=5, background_color="darkseagreen", border_color="lightgreen"):
        self._webdriver = webdriver
        self._wait_in_sec = wait_in_sec
        self._background_color = background_color
        self._border_color = border_color

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

    def highlight(self, element, background_color=None, border_color=None):
        bg_color = background_color or self._background_color
        b_color = border_color or self._border_color
        try:
            self._webdriver.execute_script(
                f"arguments[0].setAttribute('style', 'background: {bg_color}; border: 2px solid {b_color};');",
                element
            )
        except JavascriptException as e:
            logging.warning(str(e))

    def highlight_and_wait(self, element, wait_in_sec=None, background_color=None, border_color=None):
        self.highlight(element, background_color, border_color)
        wait_in_sec = wait_in_sec or self._wait_in_sec
        time.sleep(wait_in_sec)
