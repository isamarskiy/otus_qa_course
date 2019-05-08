"""
Проверка удаления продукта
"""
import time


def test_add_product(driver):
    driver.get('http://localhost/opencart/admin')
    # http://localhost/admin http://localhost/opencart/admin
    driver.find_element_by_id('input-username').send_keys('admin')
    driver.find_element_by_id('input-password').send_keys('admin')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    driver.find_element_by_xpath("//a[contains(text(),'Catalog')]").click()
    time.sleep(1)  # не успевает увидеть элемент
    driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()
    driver.find_element_by_xpath("//td[contains(text(),'Test product2')]/parent::*//input").click()
    driver.find_element_by_xpath("//button[@data-original-title='Delete']").click()
    driver.switch_to.alert.accept()
    notification = driver.find_element_by_class_name("alert.alert-success.alert-dismissible")
    notification_text = notification.text.rstrip("\n×'")
    assert notification
    assert notification_text == 'Success: You have modified products!'
