import logging
import time

from selenium.common import JavascriptException


class Highlighter:
    """
    Highlights an element by a colored border and alternating background colors
    """
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
        """
        Highlights an element by a colored border and alternating background colors
        """
        style_attrs = self._create_style_attrs(element)
        try:
            self._webdriver.execute_script(f"arguments[0].setAttribute('style', '{style_attrs}');", element)
        except JavascriptException as e:
            logging.warning(str(e))

    def highlight_and_wait(self, element, wait_in_sec=None):
        """
        Highlights an element by a colored border and alternating background colors.
        Then wait several seconds.
        """
        self.highlight(element)
        wait_in_sec = wait_in_sec or self._wait_in_sec
        time.sleep(wait_in_sec)

    def _get_next_background(self, element):
        background = self._backgrounds[0]
        style_dict = self._get_style_dict(element)
        try:
            current_background = style_dict["background"]
            index = self._backgrounds.index(current_background)
            background = self._backgrounds[index + 1]
        except (KeyError, ValueError, IndexError):
            return background
        return background

    def _create_style_attrs(self, element):
        style_dict = self._get_style_dict(element)
        # Update values
        if self._backgrounds:
            style_dict["background"] = self._get_next_background(element)
        if self._border:
            style_dict["border"] = self._border
        # Get style attributes as string
        style_attrs = ";".join([f"{key}:{value}" for key, value in style_dict.items()]) + ";"
        return style_attrs

    @staticmethod
    def _get_style_dict(element):
        attr_dict = {}
        style_attrs = element.get_attribute("style")
        if style_attrs:
            attr_list = [attr.strip() for attr in style_attrs.split(";")][:-1]
            attr_dict = dict(tuple(attr.split(": ")) for attr in attr_list)
        return attr_dict
