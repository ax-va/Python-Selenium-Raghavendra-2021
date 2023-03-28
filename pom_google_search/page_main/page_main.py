from pom.pages.page_base import PageBase
from pom_google_search.page_main.part_search_bar import PartSearchBar


class PageMain(PageBase):

    @property
    def part_search_bar(self):
        return PartSearchBar(self.driver)

    def is_ready(self):
        return self.part_search_bar.is_displayed()

    def search_for(self, text):
        self.part_search_bar.search_for(text)
        return self
