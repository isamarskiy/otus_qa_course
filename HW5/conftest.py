import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import IeOptions


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://192.168.11.205/")
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('--start-fullscreen')
        options.add_argument('--headless')
        wd = webdriver.Chrome(options=options)
        request.addfinalizer(wd.quit)
        return wd
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--start-fullscreen')
        options.add_argument('--headless')
        wd = webdriver.Firefox(options=options)
        request.addfinalizer(wd.quit)
        return wd
    else:
        options = IeOptions()
        options.add_argument('--start-fullscreen')
        # options.add_argument('--headless')
        wd = webdriver.Ie(options=options)
        request.addfinalizer(wd.quit)
        return wd

