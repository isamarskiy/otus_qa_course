"""
Проверка удаления продукта
"""
import time


def test_add_product(driver):
    driver.get('http://localhost/admin')
    # http://localhost/admin http://localhost/opencart/admin
    driver.find_element_by_id('input-username').send_keys('admin')
    driver.find_element_by_id('input-password').send_keys('admin')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    driver.find_element_by_xpath("//a[contains(text(),'Catalog')]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()
    driver.find_element_by_xpath("//td[contains(text(),'aaTest product1')]/parent::*//input").click()
    driver.find_element_by_xpath("//button[@data-original-title='Delete']").click()
    driver.switch_to.alert.accept()
    notification = driver.find_element_by_xpath("//div[contains(text(), 'Success: You have modified products')]")
    assert notification
