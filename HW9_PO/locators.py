from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    EMAIL = (By.NAME, "email")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    FORGET_PASS = (By.LINK_TEXT, "Forgotten Password")
    BUTTON_RESET = (By.XPATH, "//*[contains(text(),'Reset')]")
    ALERT_FAILURE = (By.XPATH, "//*[contains(text(), 'No match for Username and/or Password')]")


class DashboardLocators:
    CATALOG = (By.XPATH, "//a[contains(text(),'Catalog')]")
    PRODUCTS = (By.XPATH, "//a[contains(text(),'Products')]")


class ProductPageLocators:
    ADD_BUTTON = (By.XPATH, "//a[@data-original-title='Add New']")
    DELETE_BUTTON = (By.XPATH, "//button[@data-original-title='Delete']")
    EDIT_BUTTON = (By.XPATH, "//td[contains(text(), {product_name})]/parent::*//a")
    SUCCESS_ALERT = (By.XPATH, "//div[contains(text(), 'Success: You have modified products')]")
    DELETE_PRODUCT_BY_NAME = (By.XPATH, "//td[contains(text(),'aaTest')]/parent::*//input")
    # имя в локатор


class EditProductPageLocators:
    PRODUCT_NAME = (By.NAME, "product_description[1][name]")
    META_TAG_TITLE = (By.NAME, "product_description[1][meta_title]")
    TAB_DATA = (By.LINK_TEXT, "Data")
    TAB_IMAGE = (By.LINK_TEXT, "Image")
    MODEL_DATA = (By.NAME, "model")
    SAVE_BUTTON = (By.XPATH, "//button[@data-original-title='Save']")
    ADD_IMG_BUTTON = (By.XPATH, "//button[@data-original-title='Add Image']")
    EDIT_PRODUCT_BY_NAME = (By.XPATH, "//td[contains(text(), 'aaaTest_product')]/parent::*//a")
    # {product_name}
    TABLE_IMAGES_ELEMENT = (By.XPATH, "(//div[@class= 'table-responsive']//table[@id= 'images']//*//img)[last()]")
    BUTTON_EDIT_IMAGE = (By.ID, "button-image")


class DownloadPageLocators:
    FILE_NAME = (By.NAME, "download_description[1][name]")
    MASK_NAME = (By.NAME, "mask")
    INPUT_FIELD = (By.CSS_SELECTOR, "input[name='file']")
    SAVE_BUTTON = (By.XPATH, "//button[@data-original-title= 'Save']")



