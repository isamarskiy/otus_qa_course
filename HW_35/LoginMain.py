from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from HW_35.locators import LoginMainPageLocators


class LoginMain(object):

    @keyword(name="Login Main")
    def driver(self):
        options = ChromeOptions()
        options.add_argument('--headless')
        wd = webdriver.Chrome(options=options)
        return wd

    @keyword(name="open page")
    def open(self):
        url = 'https://localhost/index.php?route=account/login'
        self.driver.get(url)

    @keyword(name="set email")
    def set_username(self, email):
        self.driver.find_element(*LoginMainPageLocators.EMAIL).send_keys(email)

    @keyword(name="set password")
    def set_password(self, password):
        self.driver.find_element(*LoginMainPageLocators.PASSWORD).send_keys(password)

    @keyword(name="submit")
    def login(self):
        self.driver.find_element(*LoginMainPageLocators.SUBMIT_BUTTON).click()
        assert self.driver.title == 'My Account'

    @keyword(name="close")
    def close(self):
        self.driver.quit()
