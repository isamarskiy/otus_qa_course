def test_example(driver, request):
    """
    First test
    """
    driver.get(request.config.getoption('--url'))
    assert driver.title == 'Your Store'
