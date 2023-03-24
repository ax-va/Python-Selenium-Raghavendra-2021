from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT = 20  # seconds
POLLING_EVERY = 0.5  # second
IGNORED_EXCEPTIONS = (NoSuchElementException, )  # ignored exceptions during polling calls


class BaseClass:
    def __init__(self, driver,
                 timeout=TIMEOUT,
                 polling_every=POLLING_EVERY,
                 ignored_exceptions=IGNORED_EXCEPTIONS):
        self._driver = driver
        self._timeout = timeout
        self._polling_every = polling_every
        self._ignored_exceptions = ignored_exceptions

    @property
    def driver(self):
        return self._driver

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        self._timeout = timeout

    @property
    def polling_every(self):
        return self._polling_every

    @polling_every.setter
    def polling_every(self, polling_every):
        self._polling_every = polling_every

    @property
    def ignored_exceptions(self):
        return self._ignored_exceptions

    @ignored_exceptions.setter
    def ignored_exceptions(self, ignored_exceptions):
        self._ignored_exceptions = ignored_exceptions

    @property
    def wait(self):
        return WebDriverWait(
            driver=self._driver,
            timeout=self._timeout,
            poll_frequency=self._polling_every,
            ignored_exceptions=self._ignored_exceptions
        )

    def find_element(self, locator_by, locator_value):
        return self.driver.find_element(locator_by, locator_value)

    def find_elements(self, locator_by, locator_value):
        return self.driver.find_elements(locator_by, locator_value)

    def wait_for_presence_of_element_located(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        from pom.elements.base_element import BaseElement
        return BaseElement(self.driver, locator)
