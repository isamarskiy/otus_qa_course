import pytest
import sys
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions


def pytest_addoption(parser):
    # parser.addoption("--url", action="store", default="http://localhost/opencart")
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        print('\n Chrome browser')
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        #options.add_argument('--headless')
        wd = webdriver.Chrome(options=options)
        return wd
    elif browser == 'firefox':
        print('\n FF browser')
        options = FirefoxOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        wd = webdriver.Firefox(options=options)
        wd.maximize_window()
        return wd
    else:
        print('Unsupported browser')
        sys.exit(1)
    #yield wd
    wd.quit()
