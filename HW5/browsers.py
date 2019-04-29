def test_example(driver, request):
    """
    First test
    Запуска тестов:
    python3 -m pytest -v -s browsers.py --browser=firefox
    python3 -m pytest -v -s browsers.py --browser=chrome

    """
    driver.get(request.config.getoption('--url'))
    assert driver.title == 'Your Store'
