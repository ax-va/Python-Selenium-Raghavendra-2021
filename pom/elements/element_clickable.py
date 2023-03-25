from pom.elements.element_base import ElementBase


class ElementClickable(ElementBase):
    def click(self):
        self.find_yourself().click()
        return self
