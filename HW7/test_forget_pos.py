def test_forget_pass(driver):
    driver.get('http://localhost/admin')
    # http://localhost/admin http://localhost/opencart/admin
    assert driver.title == 'Administration'
    driver.find_element_by_link_text('Forgotten Password').click()
    assert driver.title == 'Forgot Your Password?'
    driver.find_element_by_name('email').send_keys('ya@ya.ru')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    assert driver.find_elements_by_css_selector('.alert.alert-success.alert-dismissible')
    driver.quit()
