from pom.pages_base import PagesBase
from pom_google_search.dialog_agreement.dialog_agreement import DialogAgreement
from pom_google_search.page_main.page_main import PageMain
from pom_google_search.page_results.page_results import PageResults


class Pages(PagesBase):
    def __init__(self, driver):
        pages_cls_names_google_search = {
            "DialogAgreement": DialogAgreement,
            "PageMain": PageMain,
            "PageResults": PageResults,
        }
        PagesBase.__init__(self, driver, pages_cls_names_google_search)
