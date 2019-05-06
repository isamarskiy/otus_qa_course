"""
Проверка восстановления пароля с корректной почтой
"""


def test_forget_pass(driver):
    driver.get('http://localhost/opencart/admin')
    # http://localhost/admin http://localhost/opencart/admin
    driver.find_element_by_link_text('Forgotten Password').click()
    driver.find_element_by_name('email').send_keys('ya@ya.ru')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    notification = driver.find_elements_by_css_selector('.alert.alert-success.alert-dismissible')
    assert notification
