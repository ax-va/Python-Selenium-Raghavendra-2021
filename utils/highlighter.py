import logging
import time

from selenium.common import JavascriptException


class Highlighter:
    def __init__(self, webdriver, wait_in_sec=5):
        self._webdriver = webdriver
        self._wait_in_sec = wait_in_sec

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

    def highlight_element(self, element):
        try:
            self._webdriver.execute_script(
                "arguments[0].setAttribute('style', 'background: darkseagreen; border: 2px solid lightgreen;');",
                element
            )
        except JavascriptException as e:
            logging.warning(str(e))

    def highlight_element_and_wait(self, element):
        self.highlight_element(element)
        time.sleep(self._wait_in_sec)
