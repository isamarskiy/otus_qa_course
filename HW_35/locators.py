from selenium.webdriver.common.by import By


class LoginAdminPageLocators:
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")


class LoginMainPageLocators:
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")



