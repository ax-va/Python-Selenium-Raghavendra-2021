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
        background_attr = f"background: {background};"
        border_attr = f"border: {self._border};"
        style_attrs = element.get_attribute("style")
        style_attrs = background_attr + border_attr + style_attrs
        try:
            self._webdriver.execute_script(f"arguments[0].setAttribute('style', '{style_attrs}');", element)
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
            try:
                current_background = attr_dict["background"]
                index = self._backgrounds.index(current_background)
                background = self._backgrounds[index + 1]
            except (KeyError, ValueError, IndexError):
                return background
        return background
