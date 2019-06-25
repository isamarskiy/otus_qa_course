import os
import sys
import pytest
import urllib.parse
import sqlite3
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


def my_logger(log):
    conn = sqlite3.connect('/Users/samarsky/SQLite/db_logs.db')
    cursor = conn.cursor()
    sql = 'INSERT INTO Logs VALUES (' + '\'' + str(log) + '\');'
    cursor.execute(sql)
    conn.commit()


class MyListener(AbstractEventListener):

    def before_find(self, by, value, driver):
        log = 'Поиск элемента ' + by + ' ' + value
        my_logger(log)

    def after_find(self, by, value, driver):
        log = 'Элемент найден ' + by + ' ' + value
        my_logger(log)


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="http://localhost/opencart")
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--wait", default=20000)


@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption('--browser')

    server = Server("/Users/samarsky/Documents/browsermob-proxy-2.1.4/bin/browsermob-proxy")
    server.start()
    proxy = server.create_proxy()
    url = urllib.parse.urlparse(proxy.proxy).path
    proxy.new_har()

    if browser == 'chrome':
        print('\n Chrome browser')
        capabilities = webdriver.DesiredCapabilities.CHROME.copy()
        # capabilities['timeouts'] = {'implicit': int((request.config.getoption('--wait'))), 'pageLoad': 5000}
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        options.add_argument('--proxy-server=%s' % url)
        wd = EventFiringWebDriver(webdriver.Chrome(options=options, desired_capabilities=capabilities), MyListener())
        yield wd
    elif browser == 'firefox':
        print('\n FF browser')
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        options = FirefoxOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        wd = webdriver.Firefox(options=options, desired_capabilities=capabilities)
        wd.maximize_window()
        request.addfinalizer(wd.quit)
    else:
        print('Unsupported browser')
        sys.exit(1)






