from pom.elements.base_element import BaseElement


class InputElement(BaseElement):
    def clear(self):
        self.find_yourself().clear()
        return self

    def send_keys(self, text):
        self.find_yourself().send_keys(text)
        return self

    def submit(self):
        self.find_yourself().submit()
        return self
