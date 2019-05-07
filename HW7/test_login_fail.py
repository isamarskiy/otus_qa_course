"""
Проверка авторизации с некорректными авторизационными данными
"""


def test_login_fail(driver):
    driver.get('http://localhost/opencart/admin')
    # http://localhost/admin http://localhost/opencart/admin
    driver.find_element_by_xpath("//*[contains(@name, 'username')]").send_keys('admin')
    driver.find_element_by_xpath("//*[contains(@name, 'password')]").send_keys('admin1')
    driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()
    notification = driver.find_element_by_xpath("//*[contains(text(), 'No match for Username and/or Password')]")
    assert notification
