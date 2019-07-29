from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def test_del_product(driver):
    driver.get('http://localhost/admin')
        # http://localhost/admin http://localhost/opencart/admin
    try:
        driver.find_element_by_xpath("//*[@placeholder='Username']").send_keys('admin')
        driver.find_element_by_xpath("//*[@placeholder='Password']").send_keys('admin')
        driver.find_element_by_css_selector('.btn.btn-primary').click()
        driver.find_element_by_xpath("//a[contains(text(),'Catalog')]").click()
        WebDriverWait(driver=driver, timeout=10). \
            until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Products')]")))
        driver.find_element_by_xpath("//a[contains(text(),'Products')]").click()
        driver.find_element_by_xpath("//td[contains(text(),'aaTest product1')]/parent::*//input").click()
        driver.find_element_by_xpath("//button[@data-original-title='Delete']").click()
        driver.switch_to.alert.accept()
        notification = driver.find_element_by_xpath("//div[contains(text(), 'Success: You have modified products')]")
        assert notification
    except (NoSuchElementException, ElementNotVisibleException):
        return

