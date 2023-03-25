from pom.pages.base_page import BasePage
from google_search_pom.main_page.search_bar_part import SearchBarPart


class MainPage(BasePage):

    @property
    def search_bar_part(self):
        return SearchBarPart(self.driver)

    def search_for(self, text):
        self.search_bar_part.search_for(text)
        return self
