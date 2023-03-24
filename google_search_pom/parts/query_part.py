from selenium.webdriver.common.by import By

from pom.elements.input_element import InputElement
from pom.parts.base_part import BasePart


class QueryPart(BasePart):
    QUERY_INPUT_LOCATOR = (By.NAME, "q")

    @property
    def query_input_element(self):
        return InputElement(self.driver, self.QUERY_INPUT_LOCATOR)

    def search_for(self, text):
        self.query_input_element.send_keys(text).submit()
        return self
