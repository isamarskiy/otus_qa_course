"""
Проверка добавления продукта
"""


def test_add_product(driver):
    driver.get('http://localhost/admin')
    # http://localhost/admin http://localhost/opencart/admin
    driver.find_element_by_id('input-username').send_keys('admin')
    driver.find_element_by_id('input-password').send_keys('admin')
    driver.find_element_by_css_selector('.btn.btn-primary').click()
    # driver.find_element_by_class_name('parent.collapsed').click()
    # driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()
    els = driver.find_elements_by_class_name('parent')
    for el in els:
        if el.text == 'Catalog':
            catalog = el
            break
    catalog.click()
    catalog_elements = driver.find_elements_by_tag_name('li')
    for catalog_element in catalog_elements:
        if catalog_element.text == 'Products':
            catalog_element.click()
            break
    fluids = driver.find_elements_by_class_name("container-fluid")
    for fl in fluids:
        if 'Products' in fl.text:
            action_fluid = fl
            break
    action_fluid.find_elements_by_xpath('//a[contains(@class, "btn btn-primary")]').click() # проблема
    driver.find_element_by_name('product_description[1][name]').send_keys('Test product')
    driver.find_element_by_name('product_description[1][meta_title]').send_keys('Test tag')
    driver.find_element_by_partial_link_text('tab-data').click()
    driver.find_element_by_name('model').send_keys('Test model')
    driver.find_element_by_class_name('fa.fa-save').click()
    notification = driver.find_element_by_class_name("alert.alert-success.alert-dismissible")
    new_product = driver.find_element_by_xpath("//td[contains(text(),'Test product')]")
    notification_text = notification.text.rstrip("\n×'")
    assert new_product
    assert notification
    assert notification_text == 'Success: You have modified products!'










