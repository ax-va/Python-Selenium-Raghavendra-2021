from selenium.webdriver.common.by import By

from pom.elements.clickable_element import ClickableElement
from pom.pages.base_page import BasePage


class AgreementDialog(BasePage):
    REJECT_ALL_BUTTON_LOCATOR = (By.ID, "W0wltc")

    @property
    def reject_all_button(self):
        return ClickableElement(self.driver, self.REJECT_ALL_BUTTON_LOCATOR)

    def click_on_reject_all_button(self):
        self.reject_all_button.click()
        return self
