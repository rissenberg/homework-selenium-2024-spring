from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.settings_page_locators import SettingsPageLocators
from selenium.webdriver.support import expected_conditions as EC



class SettingsPage(BasePage):
    url = 'https://ads.vk.com/hq/settings'
    locators = SettingsPageLocators()

    ERROR_INVALID_PHONE_NUMBER = 'Некорректный номер телефона'
    ERROR_EMPTY_REQUIRED_FIELD = 'Обязательное поле'
    ERROR_TOO_SHORT_INN = 'Длина ИНН должна быть 12 символов'
    ERROR_INVALID_INN = 'Некорректный ИНН'
    ERROR_INVALID_EMAIL = 'Некорректный email адрес'

    def save_button_and_cancel_button_is_visible(self) -> bool:
        return (self.is_visible(self.locators.SAVE_BUTTON) and self.is_visible(self.locators.CANCEL_BUTTON))

    def enter_phone_number(self, phone_number: str):
        phone_number_input = self.find(self.locators.PHONE_NUMBER_INPUT)
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)
        phone_number_input.send_keys(Keys.ENTER)

    def get_phone_number_error(self) -> str:
        return self.find(self.locators.ERROR_PHONE_NUMBER).text
    
    def enter_full_name(self, full_name: str):
        full_name_input = self.find(self.locators.FULL_NAME_INPUT)
        full_name_input.clear()
        full_name_input.send_keys(full_name)

    def get_full_name_field_value(self) -> str:
        return self.find(self.locators.FULL_NAME_INPUT).get_attribute('value')
    
    def enter_inn(self, inn: str):
        inn_input = self.find(self.locators.INN_INPUT)
        inn_input.clear()
        inn_input.send_keys(inn)
        inn_input.send_keys(Keys.ENTER)

    def get_inn_error(self) -> str:
        return self.find(self.locators.ERROR_INN).text

    def click_add_email_button(self):
        self.click(self.locators.ADD_EMAIL_BUTTON)

    def add_email_input_is_visible(self) -> bool:
        return self.is_visible(self.locators.ADD_EMAIL_INPUT)

    def enter_email(self, email: str):
        email_input = self.find(self.locators.ADD_EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)

    def get_email_error(self) -> str:
        return self.find(self.locators.ERROR_EMAIL).text

    def get_full_name_error(self) -> str:
        return self.find(self.locators.ERROR_FULL_NAME).text

    def click_logout_other_devices_button(self):
        self.click(self.locators.LOGOUT_OTHER_DEVICES_BUTTON)

    def logout_devices_success_message_is_visible(self) -> bool:
        return self.is_visible(self.locators.LOGOUT_OTHER_DEVICES_MESSAGE)

    def click_delete_cabinet_button(self):
        self.click(self.locators.DELETE_CABINET_BUTTON)

    def delete_cabinet_modal_page_is_visible(self) -> bool:
        return self.is_visible(self.locators.DELETE_CABINET_MODAL_PAGE)

    def click_save_button(self):
        wait = self.wait(10)
        save_button = wait.until(EC.visibility_of_element_located(self.locators.SAVE_BUTTON))
        save_button.click()

    def click_cancel_button(self):
        self.click(self.locators.CANCEL_BUTTON)

