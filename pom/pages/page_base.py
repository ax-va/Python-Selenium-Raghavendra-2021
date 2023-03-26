from pom.class_base import ClassBase
from pom.elements.element_base import ElementBase
from pom.elements.element_clickable import ElementClickable


class PageBase(ClassBase):
    def create_base_element(self, locator):
        return ElementBase(self._driver, locator)

    def create_clickable_element(self, locator):
        return self.create_base_element(locator).to_clickable()

    def create_input_element(self, locator):
        return self.create_base_element(locator).to_input()
