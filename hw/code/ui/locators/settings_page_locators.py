from selenium.webdriver.common.by import By
from ui.locators.basic_locators import BasePageLocators


class SettingsPageLocators(BasePageLocators):
    SAVE_BUTTON = (By.XPATH, "//span[text()='Сохранить']")
    CANCEL_BUTTON = (By.XPATH, "//*[contains(@class, 'FormControls_buttons__')]/button[@type='button']")

    PHONE_NUMBER_INPUT = (By.XPATH, "//*[@data-testid='general-phone']")
    ERROR_PHONE_NUMBER = (By.XPATH, "//*[contains(@class, 'Contacts_wrap__')]//*[@role='alert']/div")

    INN_INPUT = (By.XPATH, "//*[@data-testid='general-ord-inn']")
    ERROR_INN = (By.XPATH,"//div[contains(@class, 'vkuiFormItem') and child::h2/span[text()='ИНН']]/span[@role='alert']/div" )

    ADD_EMAIL_BUTTON = (By.XPATH, "//span[text()='Добавить email']")
    ADD_EMAIL_INPUT = (By.XPATH, f"//*[@data-testid='email-0']")
    ERROR_EMAIL = (By.XPATH, "//*[contains(@class, 'vkuiFormItem__removable')]//*[@role='alert']/div")

    FULL_NAME_INPUT = (By.XPATH, "//*[@data-testid='general-ord-name']")
    ERROR_FULL_NAME = (By.XPATH, "//div[contains(@class, 'vkuiFormItem') and child::h2/span[text()='ФИО']]/span[@role='alert']/div")

    LOGOUT_OTHER_DEVICES_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Выйти из других устройств']")
    LOGOUT_OTHER_DEVICES_MESSAGE = (By.XPATH, "//*[contains(@class, 'Snackbar_success__')]")

    DELETE_CABINET_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Удалить кабинет']")
    DELETE_CABINET_MODAL_PAGE = (By.XPATH, "//*[contains(@class, 'DeleteAccountConfirmModal_')]")
