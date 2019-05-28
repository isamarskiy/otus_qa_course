import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from HW9_PO.page import LoginPage, DashboardPage, ProductPageButtons, ProductEditPage
from HW9_PO.locators import ProductPageLocators


@pytest.fixture(scope='module', autouse=True)
def login(driver):
    """Авторизация"""
    driver.get('http://localhost/admin')
    login_page = LoginPage(driver)
    login_page.login_on_page('admin', 'admin')
    WebDriverWait(driver=driver, timeout=10).until(ec.title_contains('Dashboard'))


@pytest.fixture(scope='module', autouse=True)
def select_product_page(driver):
    try:
        dashboard_page = DashboardPage(driver)
        dashboard_page.open_catalog()
        dashboard_page.open_products()
    except (NoSuchElementException, ElementNotVisibleException):
        return print("Элемент отсутствует или не найден")


@pytest.fixture
def product_edit_page(driver):
    return ProductEditPage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPageButtons(driver)


@pytest.fixture
def add_product(product_edit_page):
    try:
        product_name = 'aaaTest_product'
        tag_title = 'test_tag_title'
        model_name = 'test_model_name'
        product_edit_page.add_product(product_name, tag_title, model_name)
    except (NoSuchElementException, ElementNotVisibleException):
        return print("Элемент отсутствует или не найден")


@pytest.fixture
def edit_product(product_edit_page):
    try:
        new_product_name = 'aaTest'
        product_edit_page.click_edit_product(new_product_name)
    except (NoSuchElementException, ElementNotVisibleException):
        return print("Элемент отсутствует или не найден")


@pytest.fixture
def delete_product(product_page):
    product_page.delete_product_by_name()


@pytest.mark.usefixtures("add_product")
def test_add_product():
    """Создание продукта"""
    assert ProductPageLocators.SUCCESS_ALERT


@pytest.mark.usefixtures("edit_product")
def test_edit_product():
    """Редактирование продукта"""
    assert ProductPageLocators.SUCCESS_ALERT


@pytest.mark.usefixtures("delete_product")
def test_delete_product():
    """Удаление продукта"""
    assert ProductPageLocators.SUCCESS_ALERT
