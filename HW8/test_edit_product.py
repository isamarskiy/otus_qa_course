def test_add_product(driver):
    driver.get('http://localhost/admin')
    # http://localhost/admin http://localhost/opencart/admin
    driver.find_element_by_id('input-username').send_keys('admin')
    driver.find_element_by_id('input-password').send_keys('admin')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    driver.fi