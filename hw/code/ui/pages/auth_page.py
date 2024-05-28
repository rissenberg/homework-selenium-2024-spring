from ui.pages.base_page import BasePage
from ui.locators.auth_page_locators import AuthPageLocators
from selenium.webdriver.support import expected_conditions as EC
import time


class AuthPage(BasePage):
    locators = AuthPageLocators()

    def login(self, login, password):
        mail_auth_button = self.wait_until(EC.visibility_of_element_located(self.locators.MAIL_RU_AUTH_BUTTON), 10)
        mail_auth_button.click()

        login_input = self.wait_until(EC.visibility_of_element_located(self.locators.MAIL_RU_LOGIN), 10)
        login_input.clear()
        login_input.send_keys(login)

        self.click(self.locators.MAIL_RU_NEXT_BUTTON)

        password_input = self.wait_until(EC.visibility_of_element_located(self.locators.MAIL_RU_PASSWORD), 10)
        password_input.clear()
        password_input.send_keys(password)

        self.click(self.locators.MAIL_RU_SUBMIT_BUTTON)
