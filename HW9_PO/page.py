from HW9_PO.locators import LoginPageLocators, DashboardLocators, EditPageLocators, ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def set_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def login(self):
        self.driver.finde_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    def login_on_page(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.login()


class DashboardPage:

    def open_catalog(self):
        self.driver.find_element(DashboardLocators.CATALOG).click()

    def open_products(self):
        self.driver.find_element(DashboardLocators.PRODUCTS).click()

    def select_product(self, driver):
        self.open_catalog()
        self.open_products()
        WebDriverWait(driver=driver, timeout=10).until(ec.title_contains('Products'))






