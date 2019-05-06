"""
Проверка авторизации с некорректными авторизационными данными
"""


def test_login_fail(driver):
    driver.get('http://localhost/opencart/admin')
    # http://localhost/admin http://localhost/opencart/admin
    driver.find_element_by_id('input-username').send_keys('admin')
    driver.find_element_by_id('input-password').send_keys('admin1')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    notification = driver.find_element_by_css_selector('.alert.alert-danger.alert-dismissible')
    assert notification
