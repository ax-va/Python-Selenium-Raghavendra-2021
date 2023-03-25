from selenium.webdriver.common.by import By

from pom.elements.input_element import InputElement
from pom.parts.base_part import BasePart


class SearchBarPart(BasePart):
    INPUT_LOCATOR = (By.NAME, "q")

    @property
    def input_element(self):
        return InputElement(self.driver, self.INPUT_LOCATOR)

    def search_for(self, text):
        self.input_element.send_keys(text).submit()
        return self
