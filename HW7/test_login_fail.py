def test_login_fail(driver):
    driver.get('http://localhost/admin')
    # http://localhost/admin http://localhost/opencart/admin
    assert driver.title == 'Administration'
    driver.find_element_by_id('input-username').send_keys('admin')
    driver.find_element_by_id('input-password').send_keys('admin1')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    assert driver.find_element_by_css_selector('.alert.alert-danger.alert-dismissible')
    driver.quit()
