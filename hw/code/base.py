import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

    def is_opened(self, url, timeout=None):
        if timeout is None:
            timeout = 5

        try:
            WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
            return True
        except:
            raise Exception(f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

