from pom.class_base import ClassBase


class ElementBase(ClassBase):
    def __init__(self, driver, locator):
        ClassBase.__init__(self, driver)
        self._locator = locator

    @property
    def locator(self):
        return self._locator

    @property
    def locator_by(self):
        return self._locator[0]

    @property
    def locator_value(self):
        return self._locator[1]

    def find_yourself(self):
        return self.find_element(self.locator_by, self.locator_value)

    def to_input(self):
        from pom.elements.element_input import ElementInput
        return ElementInput(self.driver, self.locator)

    def to_clickable(self):
        from pom.elements.element_clickable import ElementClickable
        return ElementClickable(self.driver, self.locator)
