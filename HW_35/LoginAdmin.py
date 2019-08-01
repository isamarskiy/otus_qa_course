from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from HW_35.locators import LoginAdminPageLocators


class LoginAdmin(object):

    @keyword(name="Login Admin")
    def driver(self):
        options = ChromeOptions()
        options.add_argument('--headless')
        wd = webdriver.Chrome(options=options)
        return wd

    @keyword(name="open page")
    def open(self):
        url = 'http://localhost/admin/'
        self.driver.get(url)

    @keyword(name="set username")
    def set_username(self, username):
        self.driver.find_element(*LoginAdminPageLocators.USERNAME).send_keys(username)

    @keyword(name="set password")
    def set_password(self, password):
        self.driver.find_element(*LoginAdminPageLocators.PASSWORD).send_keys(password)

    @keyword(name="submit")
    def submit(self):
        self.driver.find_element(*LoginAdminPageLocators.SUBMIT_BUTTON).click()
        assert self.driver.title == 'Dashboard'

    @keyword(name="close")
    def close(self):
        self.driver.quit()

