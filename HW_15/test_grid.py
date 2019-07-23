import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Remote("http://10.0.2.15:5555/wd/hub", desired_capabilities={"browserName": "firefox"})
    request.addfinalazier(wd.quit)
    return wd


def test_grid(driver):
    driver.get('http://www.google.com')
    print(driver.title)
    assert driver.title == 'Google'
