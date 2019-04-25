import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import IeOptions


@pytest.fixture()
def chrome_browser(request):
    options = ChromeOptions()
    options.add_argument('--start-fullscreen')
    options.add_argument('--headless')
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture()
def firefox_browser(request):
    options = FirefoxOptions()
    options.add_argument('--start-fullscreen')
    options.add_argument('--headless')
    wd = webdriver.Firefox(options=options)
    request.addfinalizer(wd.quit)
    return wd


@pytest.fixture()
def ie_browser(request):
    options = IeOptions()
    options.add_argument('--start-fullscreen')
    options.add_argument('--headless')
    wd = webdriver.Ie(options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_example(ie_browser):
    """
    First test
    """
    ie_browser.get("http://10.0.2.15/opencart/")
    ie_browser.save_screenshot('test_ScreenShot1.png')
    #assert chrome_browser.find_element_by_class_name('header2-menu__phone').text == '+7 499 959-43-99'
