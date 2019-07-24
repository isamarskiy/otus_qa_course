from selenium.webdriver.common.action_chains import ActionChains
import allure


@allure.title('DnD first test')
@allure.description('Success test')
def test_dnd(driver):
    """ Проверка перетаскивания элементов drag and drop"""
    driver.get('http://demo23.opencart.pro/admin/')

    driver.find_element_by_name('username').send_keys('demo')
    driver.find_element_by_name('password').send_keys('demo')
    driver.find_element_by_xpath("//button[@type= 'submit']").click()

    driver.find_element_by_id('menu-design').click()
    driver.find_element_by_xpath("//a[contains(text(), 'Конструктор Меню')]").click()

    source1 = driver.find_element_by_xpath("//span[contains(text(), 'Macs')]")
    source2 = driver.find_element_by_xpath("//span[contains(text(), 'Windows')]")
    action = ActionChains(driver)
    assert source1.location['y'] < source2.location['y']
    action.drag_and_drop(source1, source2).perform()
    assert source2.location['y'] < source1.location['y']
    driver.save_screenshot('test.png')


@allure.title('DnD second test')
@allure.description('Failed test')
def test_dnd_fail(driver):
    """ Проверка перетаскивания элементов drag and drop"""
    driver.get('http://demo23.opencart.pro/admin/')

    driver.find_element_by_name('username').send_keys('demo')
    driver.find_element_by_name('password').send_keys('demo')
    driver.find_element_by_xpath("//button[@type= 'submit']").click()

    driver.find_element_by_id('menu-design').click()
    driver.find_element_by_xpath("//a[contains(text(), 'Конструктор Меню')]").click()

    source1 = driver.find_element_by_xpath("//span[contains(text(), 'Macs')]")
    source2 = driver.find_element_by_xpath("//span[contains(text(), 'Windows')]")
    action = ActionChains(driver)
    assert source1.location['y'] > source2.location['y']
    action.drag_and_drop(source1, source2).perform()
    assert source2.location['y'] > source1.location['y']
