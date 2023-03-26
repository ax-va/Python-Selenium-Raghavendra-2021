class PagesBase:
    def __init__(self, driver, pages_cls_names):
        self._driver = driver
        self._cache_pages = {}
        self._pages_cls_names = pages_cls_names

    def get(self, page_cls_name, *args, **kwargs):
        page = self._cache_pages.get(page_cls_name)
        if page is not None:
            return page
        else:
            page_cls = self._pages_cls_names.get(page_cls_name)
            if page_cls is None:
                raise ValueError(f"Page class '{page_cls_name}' missing")
            page = page_cls(self._driver, *args, **kwargs)
            self._cache_pages[page_cls_name] = page
            return page
