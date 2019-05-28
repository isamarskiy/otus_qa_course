from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from HW9_PO.locators import LoginPageLocators, DashboardLocators, EditProductPageLocators, ProductPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """ Описание страницы логина"""

    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def login(self):
        self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    def forget_password(self):
        self.driver.find_element(*LoginPageLocators.FORGET_PASS).click()

    def login_on_page(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.login()


class DashboardPage(BasePage):
    """Описание главной страницы дашборда"""

    def open_catalog(self):
        return self.driver.find_element(*DashboardLocators.CATALOG).click()

    def open_products(self):
        self.driver.find_element(*DashboardLocators.PRODUCTS).click()
        WebDriverWait(driver=self.driver, timeout=10).until(ec.title_contains('Products'))

    def select_product_page(self):
        """Выбор страницы продуктов"""
        self.open_catalog()
        self.open_products()


class ProductPageButtons(BasePage):
    """Описание элементов на старнице продукты"""

    def click_add_button(self):
        """Нажатие кнопки добавить"""
        return self.driver.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def click_del_button(self):
        """Нажатие кнопки удалить"""
        return self.driver.find_element(*ProductPageLocators.DELETE_BUTTON).click()

    def click_edit_button(self):
        """Нажатие кнопки редактировать"""
        return self.driver.find_element(*ProductPageLocators.EDIT_BUTTON).click()

    def delete_product_by_name(self):
        """Удаление продукта по названию"""
        self.driver.find_element(*ProductPageLocators.DELETE_PRODUCT_BY_NAME).click()
        # передавать в локатор название продукта
        self.click_del_button()
        self.driver.switch_to.alert.accept()

    def select_edit_product_by_name(self):
        """Выбор продукта по названию"""
        return self.driver.find_element(*EditProductPageLocators.EDIT_PRODUCT_BY_NAME).click()
        # передавать в локатор параметр


class ProductEditPage(ProductPageButtons):
    """Описание страницы редактирования продукта"""

    def set_name_product(self, product_name):
        """Заполнение названия продукта"""
        return self.driver.find_element(*EditProductPageLocators.PRODUCT_NAME).send_keys(product_name)

    def set_tag_title(self, tag_title):
        """Заполнение тэга"""
        return self.driver.find_element(*EditProductPageLocators.META_TAG_TITLE).send_keys(tag_title)

    def select_tab(self):
        """Выбрать вкладку"""
        return self.driver.find_element(*EditProductPageLocators.TAB_DATA).click()

    def set_model_name(self, model_name):
        """Заполнение модели"""
        return self.driver.find_element(*EditProductPageLocators.MODEL_DATA).send_keys(model_name)

    def save_button(self):
        """Нажатие кнопки сохранить"""
        return self.driver.find_element(*EditProductPageLocators.SAVE_BUTTON).click()

    def clear_name(self):
        """Удаление имени"""
        return self.driver.find_element(*EditProductPageLocators.PRODUCT_NAME).clear()

    def add_product(self, product_name, tag_title, model_name):
        """Добавление нового продукта"""
        self.click_add_button()
        self.set_name_product(product_name)
        self.set_tag_title(tag_title)
        self.select_tab()
        self.set_model_name(model_name)
        self.save_button()
        assert self.driver.find_element(*ProductPageLocators.SUCCESS_ALERT)

    def click_edit_product(self, new_product_name):
        """Редактирование продукта(выбор по имени)"""
        self.select_edit_product_by_name()
        self.clear_name()
        self.set_name_product(new_product_name)
        self.save_button()
        assert self.driver.find_element(*ProductPageLocators.SUCCESS_ALERT)















