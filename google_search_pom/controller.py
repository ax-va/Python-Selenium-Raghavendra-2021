from google_search_pom.pages.agreement_dialog import AgreementDialog
from google_search_pom.pages.main_page import MainPage
from google_search_pom.pages.results_page import ResultsPage

GOOGLE_SEARCH_POM_PAGES = {
    "AgreementDialog": AgreementDialog,
    "MainPage": MainPage,
    "ResultsPage": ResultsPage,
}


class Controller:
    def __init__(self, driver):
        self._driver = driver
        self._pages_cache = {}

    def get_page(self, page_cls_name, *args, **kwargs):
        page = self._pages_cache.get(page_cls_name)
        if page is not None:
            return page
        else:
            page_cls = GOOGLE_SEARCH_POM_PAGES.get(page_cls_name)
            if page_cls is None:
                raise ValueError(f"Page class '{page_cls_name}' missing")
            page = page_cls(self._driver, *args, **kwargs)
            self._pages_cache[page_cls_name] = page
            return page
