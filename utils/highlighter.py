import logging
import time

from selenium.common import JavascriptException


class Highlighter:
    """ Highlights an element by a colored border and alternating background colors """
    def __init__(self,
                 webdriver,
                 wait_in_sec=2,
                 backgrounds=("darkseagreen", "peachpuff", "pink"),
                 border="2px solid lightgreen"):
        self._webdriver = webdriver
        self._wait_in_sec = wait_in_sec
        self._backgrounds = backgrounds
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

    def highlight(self, element):
        background = self._get_next_background(element)
        background_values = f"background: {background};"
        border_values = f"border: {self._border};"
        style_values = background_values + border_values
        try:
            self._webdriver.execute_script(f"arguments[0].setAttribute('style', '{style_values}');", element)
        except JavascriptException as e:
            logging.warning(str(e))

    def highlight_and_wait(self, element, wait_in_sec=None):
        self.highlight(element)
        wait_in_sec = wait_in_sec or self._wait_in_sec
        time.sleep(wait_in_sec)

    def _get_next_background(self, element):
        background = self._backgrounds[0]
        style_attribute = element.get_attribute("style")
        if style_attribute:
            attr_list = [attr.strip() for attr in style_attribute.split(";")][:-1]
            attr_dict = dict(tuple(attr.split(": ")) for attr in attr_list)
            current_background = attr_dict.get("background")
            if current_background:
                for index, bgd in enumerate(self._backgrounds):
                    if current_background == bgd:
                        next_index = index + 1
                        if next_index != len(self._backgrounds):
                            background = self._backgrounds[next_index]
                        break
        return background
