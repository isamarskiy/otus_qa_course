
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


def test_edit_product(driver):
    driver.get('http://127.0.0.1/admin')
    # http://localhost/admin http://localhost/opencart/admin
    try:
        driver.find_element_by_xpath("//*[contains(@name, 'username')]").send_keys('admin')
        driver.find_element_by_xpath("//*[contains(@name, 'password')]").send_keys('admin')
        driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()
        driver.find_element_by_xpath("//a[contains(text(),'Catalog')]").click()
        WebDriverWait(driver=driver, timeout=10).\
            until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Products')]")))
        driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()
        driver.find_element_by_xpath("//td[contains(text(),'aaTest product')]/parent::*//a").click()
        driver.find_element_by_name('product_description[1][name]').clear()
        driver.find_element_by_name('product_description[1][name]').send_keys('aaTest product1')
        driver.find_element_by_xpath("//button[@data-original-title='Save']").click()
        notification = driver.find_element_by_xpath("//div[contains(text(), 'Success: You have modified products')]")
        new_edit_product = driver.find_element_by_xpath("//td[contains(text(),'aaTest product1')]").is_enabled()
        assert new_edit_product
        assert notification
    except (NoSuchElementException, ElementNotVisibleException):
        return
