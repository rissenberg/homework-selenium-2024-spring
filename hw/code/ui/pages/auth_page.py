from ui.pages.base_page import BasePage
from ui.locators.auth_page_locators import AuthPageLocators
from selenium.webdriver.support import expected_conditions as EC
import time


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def login(self, login, password):
        wait = self.wait(10)
        mail_auth_button = wait.until(EC.visibility_of_element_located(self.locators.MAIL_RU_AUTH_BUTTON))
        mail_auth_button.click()

        login_input = wait.until(EC.visibility_of_element_located(self.locators.MAIL_RU_LOGIN))
        login_input.clear()
        login_input.send_keys(login)

        self.click(self.locators.MAIL_RU_NEXT_BUTTON)

        password_input = wait.until(EC.visibility_of_element_located(self.locators.MAIL_RU_PASSWORD))
        password_input.clear()
        password_input.send_keys(password)

        self.click(self.locators.MAIL_RU_SUBMIT_BUTTON)
