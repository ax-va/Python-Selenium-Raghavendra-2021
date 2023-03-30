from pom.elements.element_base import ElementBase


class ElementInput(ElementBase):
    def clear(self):
        self.find_this_element().clear()
        return self

    def send_keys(self, text):
        self.find_this_element().send_keys(text)
        return self

    def submit(self):
        self.find_this_element().submit()
        return self
