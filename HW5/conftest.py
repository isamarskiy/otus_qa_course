import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import IeOptions


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost/opencart")
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        print('\n Chrome browser')
        options = ChromeOptions()
        options.add_argument('--start-fullscreen')
        options.add_argument('--headless')
        wd = webdriver.Chrome(options=options)
        request.addfinalizer(wd.quit)
        return wd
    elif browser == 'firefox':
        print('\n FF browser')
        options = FirefoxOptions()
        options.add_argument('--start-fullscreen')
        options.add_argument('--headless')
        wd = webdriver.Firefox(options=options)
        request.addfinalizer(wd.quit)
        return wd
    else:
        print('\n IE browser')
        options = IeOptions()
        # options.add_argument('headless_ie_selenium')
        wd = webdriver.Ie(options=options)
        wd.fullscreen_window()
        request.addfinalizer(wd.quit)
        return wd

