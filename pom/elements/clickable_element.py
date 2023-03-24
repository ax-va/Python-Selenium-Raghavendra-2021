from pom.elements.base_element import BaseElement


class ClickableElement(BaseElement):
    def click(self):
        self.find_yourself().click()
        return self
