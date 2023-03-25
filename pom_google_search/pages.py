from pom_google_search.dialog_agreement.dialog_agreement import DialogAgreement
from pom_google_search.page_main.page_main import PageMain
from pom_google_search.page_results.page_results import PageResults

PAGES_POM_GOOGLE_SEARCH = {
    "DialogAgreement": DialogAgreement,
    "PageMain": PageMain,
    "PageResults": PageResults,
}


class Pages:
    def __init__(self, driver):
        self._driver = driver
        self._pages_cache = {}

    def get(self, page_cls_name, *args, **kwargs):
        page = self._pages_cache.get(page_cls_name)
        if page is not None:
            return page
        else:
            page_cls = PAGES_POM_GOOGLE_SEARCH.get(page_cls_name)
            if page_cls is None:
                raise ValueError(f"Page class '{page_cls_name}' missing")
            page = page_cls(self._driver, *args, **kwargs)
            self._pages_cache[page_cls_name] = page
            return page
