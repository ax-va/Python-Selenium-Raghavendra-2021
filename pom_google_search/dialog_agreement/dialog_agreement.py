from selenium.webdriver.common.by import By

from pom.elements.element_clickable import ElementClickable
from pom.pages.page_base import PageBase


class DialogAgreement(PageBase):
    LOCATOR_FOR_BUTTON_REJECT_ALL = (By.ID, "W0wltc")

    @property
    def button_reject_all(self):
        return ElementClickable(self.driver, self.LOCATOR_FOR_BUTTON_REJECT_ALL)

    def reject_all(self):
        self.button_reject_all.click()
        return self
