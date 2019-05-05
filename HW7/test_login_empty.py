def test_login_page(driver):
    driver.get('http://localhost/admin')
    # http://localhost/admin http://localhost/opencart/admin
    assert driver.title == 'Administration'
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    assert driver.find_elements_by_css_selector('.alert.alert-danger.alert-dismissible')
    driver.quit()
