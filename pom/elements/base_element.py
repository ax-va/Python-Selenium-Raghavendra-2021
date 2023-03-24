from pom.base_class import BaseClass


class BaseElement(BaseClass):
    def __init__(self, driver, locator):
        BaseClass.__init__(self, driver)
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

    def to_input_element(self):
        from pom.elements.input_element import InputElement
        return InputElement(self.driver, self.locator)

    def to_clickable_element(self):
        from pom.elements.clickable_element import ClickableElement
        return ClickableElement(self.driver, self.locator)
