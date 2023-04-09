from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT = 20  # seconds
POLLING_EVERY = 0.1  # second
IGNORED_EXCEPTIONS = (NoSuchElementException, )  # ignored exceptions during polling calls


class ClassBase:
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
            driver=self.driver,
            timeout=self.timeout,
            poll_frequency=self.polling_every,
            ignored_exceptions=self.ignored_exceptions
        )

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_presence_of_element_located(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
