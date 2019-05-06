"""
Проверка входа без ввода логина и пароля
"""

def test_login_page(driver):
    driver.get('http://localhost/opencart/admin')
    # http://localhost/admin http://localhost/opencart/admin
    assert driver.title == 'Administration'
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    notification = driver.find_elements_by_css_selector('.alert.alert-danger.alert-dismissible')
    assert notification

