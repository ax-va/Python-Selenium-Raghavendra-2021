from pom.pages.base_page import BasePage
from google_search_pom.parts.query_part import QueryPart


class MainPage(BasePage):

    @property
    def query_part(self):
        return QueryPart(self.driver)

    def search_for(self, text):
        self.query_part.search_for(text)
        return self
