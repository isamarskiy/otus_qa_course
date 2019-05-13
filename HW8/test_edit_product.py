"""
Проверка редактирования продукта
"""

import time


def test_edit_product(driver):
    driver.get('http://localhost/admin')
    # http://localhost/admin http://localhost/opencart/admin
    driver.find_element_by_xpath("//*[contains(@name, 'username')]").send_keys('admin')
    driver.find_element_by_xpath("//*[contains(@name, 'password')]").send_keys('admin')
    driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Catalog')]").click()
    time.sleep(1)  # не успевает увидеть элемент
    driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()
    driver.find_element_by_xpath("//td[contains(text(),'aaTest product')]/parent::*//a").click()
    driver.find_element_by_name('product_description[1][name]').clear()
    driver.find_element_by_name('product_description[1][name]').send_keys('aaTest product1')
    driver.find_element_by_xpath("//button[@data-original-title='Save']").click()
    notification = driver.find_element_by_xpath("//div[contains(text(), 'Success: You have modified products')]")
    new_product = driver.find_element_by_xpath("//td[contains(text(),'aaTest product1')]").is_enabled()
    assert new_product
    assert notification

