import sys
import pytest
import logging
import urllib.parse
from logging import Logger
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


def my_logger(log_name):
    logger: Logger = logging.getLogger("Logs")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('logs/' + log_name + '.log', mode='w')
    # fh = logging.FileHandler("logs/new.log", mode='w')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

# logging.basicConfig(filename="logs/sample.log", filemode='w',  level=logging.INFO,
#                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class MyListener(AbstractEventListener):

    def __init__(self, logger: Logger):
        self.logger: Logger = logger

    def before_find(self, by, value, driver):
        # logging.info('Поиск элемента ' + by + ' ' + value)
        self.logger.info('Поиск элемента ' + by + ' ' + value)

    def after_find(self, by, value, driver):
        # logging.info('Элемент найден ' + by + ' ' + value)
        self.logger.info('Элемент найден ' + by + ' ' + value)

    def on_exception(self, exception, driver):
        driver.save_screenshot('screenshots/new_ex.png')
        # logging.error('Error')
        self.logger.exception(exception)


def pytest_addoption(parser):
    # parser.addoption("--url", action="store", default="http://localhost/opencart")
    parser.addoption("--browser", action="store", default="firefox")
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
        capabilities['timeouts'] = {'implicit': int((request.config.getoption('--wait'))), 'pageLoad': 5000}
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        options = ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--headless')
        options.add_argument('--proxy-server=%s' % url)
        wd = webdriver.Chrome(options=options, desired_capabilities=capabilities)
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

    print(proxy.har)
    logger = my_logger('Logs')
    logged_driver = EventFiringWebDriver(wd, MyListener(logger))
    yield logged_driver

    if browser == 'chrome':
        browser_logger = my_logger('BrowsersLogs')
        for l in logged_driver.get_log("browser"):
            browser_logger.info(l)
    logged_driver.quit()





