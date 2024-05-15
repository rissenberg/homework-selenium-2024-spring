from selenium.webdriver.common.by import By
from ui.locators.basic_locators import BasePageLocators


class BudgetPageLocators(BasePageLocators):
    REPLENISH_BUDGET_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Пополнить счёт']")
    REPLENISHMENT_WINDOW = (By.ID, "_modal_17")

    CLOSE_WINDOW_BUTTON = (By.XPATH, "//*[@aria-label='Закрыть']")

    SUM_INPUT = (By.NAME, "amount")
    SUM_WITHOUT_VAT_INPUT = (By.NAME, "amountWithoutVat")

    ERROR_ALERT = (By.XPATH, "//*[@role='alert']")

    SUBMIT_BUTTON = (By.XPATH, "//*[contains(@class, 'CreateInvoiceModal_button__')]")

    PAY_WINDOW = (By.XPATH, "//iframe[contains(@class, 'CreateInvoiceModal_iframe')]")
