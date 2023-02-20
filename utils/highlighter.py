import logging
import time

from selenium.common import JavascriptException


class Highlighter:
    def __init__(self, webdriver, wait_in_sec=5, background="darkseagreen", border="2px solid lightgreen"):
        self._webdriver = webdriver
        self._wait_in_sec = wait_in_sec
        self._background = background
        self._border = border

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

    def highlight(self, element, background=None, border=None):
        background_value = "" if background is False else f"background: {background or self._background};"
        border_value = "" if border is False else f"border: {border or self._border};"
        style_value = background_value + border_value
        try:
            self._webdriver.execute_script(f"arguments[0].setAttribute('style', '{style_value}');", element)
        except JavascriptException as e:
            logging.warning(str(e))

    def highlight_and_wait(self, element, wait_in_sec=None, background=None, border=None):
        self.highlight(element, background, border)
        wait_in_sec = wait_in_sec or self._wait_in_sec
        time.sleep(wait_in_sec)
