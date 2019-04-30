import pytest
import time


def test_login_page(driver):
    driver.get('http://localhost/opencart/admin')
    assert driver.title == 'Administration'
    driver.find_element_by_id('input-username').send_keys('admin')
    driver.find_element_by_id('input-password').send_keys('admin')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    assert driver.title == 'Dashboard'
    driver.quit()


def test_login_fail(driver):
    driver.get('http://localhost/opencart/admin')
    assert driver.title == 'Administration'
    driver.find_element_by_id('input-username').send_keys('admin')
    driver.find_element_by_id('input-password').send_keys('admin1')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    assert driver.find_element_by_css_selector('.alert.alert-danger.alert-dismissible')
    driver.quit()


def test_forget_pass(driver):
    driver.get('http://localhost/opencart/admin')
    assert driver.title == 'Administration'
    driver.find_element_by_link_text('Forgotten Password').click()
    assert driver.title == 'Forgot Your Password?'
    driver.find_element_by_name('email').send_keys('ya@ya.ru')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    assert driver.find_element_by_css_selector('alert.alert-success.alert-dismissible') == ' An email with a ' \
                                                                                           'confirmation link has ' \
                                                                                           'been sent your admin ' \
                                                                                           'email address.'




    






