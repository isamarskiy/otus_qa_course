import sys
import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions


def pytest_addoption(parser):
    # parser.addoption("--url", action="store", default="http://localhost/opencart")
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--wait", default=20000)


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        print('\n Chrome browser')
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        capabilities['timeouts'] = {'implicit': int((request.config.getoption('--wait'))), 'pageLoad': 5000}
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')
        wd = webdriver.Chrome(options=options, desired_capabilities=capabilities)
        request.addfinalizer(wd.quit)
        return wd
    elif browser == 'firefox':
        print('\n FF browser')
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        capabilities['timeouts'] = {'implicit': int((request.config.getoption('--wait'))), 'pageLoad': 5000}
        options = FirefoxOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        wd = webdriver.Firefox(options=options, desired_capabilities=capabilities)
        wd.maximize_window()
        request.addfinalizer(wd.quit)
        return wd
    else:
        print('Unsupported browser')
        sys.exit(1)
    #yield wd
    wd.quit()


