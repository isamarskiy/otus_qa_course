"""
Проверка добавления продукта
"""


def test_add_product(driver):
    driver.get('http://localhost/admin')
    # http://localhost/admin http://localhost/opencart/admin
    driver.find_element_by_id('input-username').send_keys('admin')
    driver.find_element_by_id('input-password').send_keys('admin')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    driver.find_element_by_xpath("//a[contains(text(),'Catalog')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()
    driver.find_element_by_xpath("//a[@data-original-title='Add New']").click()
    driver.find_element_by_name('product_description[1][name]').send_keys('aaTest product')
    driver.find_element_by_name('product_description[1][meta_title]').send_keys('Test tag1')
    driver.find_element_by_partial_link_text('Data').click()
    driver.find_element_by_name('model').send_keys('Test model')
    driver.find_element_by_xpath("//button[@data-original-title='Save']").click()
    notification = driver.find_element_by_xpath("//div[contains(text(), 'Success: You have modified products')]")
    new_product = driver.find_element_by_xpath("//td[contains(text(),'aaTest product')]").is_enabled()
    assert new_product
    assert notification











