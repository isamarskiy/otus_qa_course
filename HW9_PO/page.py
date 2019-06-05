import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from urllib.parse import urlparse, parse_qs
from HW9_PO.locators import LoginPageLocators, DashboardLocators, EditProductPageLocators, ProductPageLocators, \
    DownloadPageLocators


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

    def select_tab_image(self):
        """Выбрать вкладку Image"""
        return self.driver.find_element(*EditProductPageLocators.TAB_IMAGE).click()

    def set_model_name(self, model_name):
        """Заполнение модели"""
        return self.driver.find_element(*EditProductPageLocators.MODEL_DATA).send_keys(model_name)

    def save_button(self):
        """Нажатие кнопки сохранить"""
        return self.driver.find_element(*EditProductPageLocators.SAVE_BUTTON).click()

    def clear_name(self):
        """Удаление имени"""
        return self.driver.find_element(*EditProductPageLocators.PRODUCT_NAME).clear()

    def add_im_button(self):
        """Нажатие кнопки добавить изображение"""
        return self.driver.find_element(*EditProductPageLocators.ADD_IMG_BUTTON).click()

    def click_on_image(self):
        return self.driver.find_element(*EditProductPageLocators.TABLE_IMAGES_ELEMENT).click()

    def click_on_edit_im(self):
        return self.driver.find_element(*EditProductPageLocators.BUTTON_EDIT_IMAGE).click()

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


class DownloadPage(BasePage):

    def upload_file(self, user_token, filename, name, mask):
        """Процесс описания загрузки файла"""
        self.driver.find_element(*DownloadPageLocators.FILE_NAME).send_keys(name)
        self.driver.find_element(*DownloadPageLocators.MASK_NAME).send_keys(mask)
        create_form = "$('body').prepend('<form enctype=\"multipart/form-data\" " \
                      "id=\"form-upload\" style=\"display: none;\"><input type=\"file\" name=\"file\" /></form>');"
        self.driver.execute_script(create_form)
        self.driver.find_element(*DownloadPageLocators.INPUT_FIELD).send_keys(filename)
        upload_js = ("$.ajax({"  # скрипт загрузки файла
                     "url: 'index.php?route=catalog/download/upload&user_token=") + user_token + ("',"
                     "type: 'post',"
                     "dataType: 'json',"
                     "data: new FormData($('#form-upload')[0]),"
                     "cache: false,"
                     "contentType: false,"
                     "processData: false,"
                     "beforeSend: function() {"
                     "  $('#button-upload').button('loading');"
                     "},"
                     "complete: function() {"
                     "  $('#button-upload').button('reset');"
                     "},"
                     "success: function(json) {"
                     "  if (json['error']) {"
                     "    alert(json['error']);"
                     "  }"
                     "  if (json['success']) {"
                     "    alert(json['success']);"
                     "    $('input[name=\\'filename\\']').val(json['filename']);"
                     "    $('input[name=\\'mask\\']').val(json['mask']);"
                     "  }"
                     "},"
                     "error: function(xhr, ajaxOptions, thrownError) {"
                     "  alert(thrownError + \"\\r\\n\" + xhr.statusText + \"\\r\\n\" + xhr.responseText);"
                     "}"
                     "});")
        self.driver.execute_script(upload_js)

    def click_save_button(self):
        return self.driver.find_element(*DownloadPageLocators.SAVE_BUTTON).click()

    def new_row_in_table(self, name):
        return self.driver.find_element_by_xpath("//table//tbody/*/td[contains(text(), '%s')]" % name)
















