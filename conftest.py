import pytest
from selene.support.shared import config, browser


@pytest.fixture(scope='function', autouse=False)
def init_config():
    browser.config.browser_name = 'chrome'
    config.timeout = 2
    config.window_width = 1980
    config.window_height = 1080


@pytest.fixture(scope='function', autouse=False)
def open_browser(init_config):
    browser.open('https://google.com')
