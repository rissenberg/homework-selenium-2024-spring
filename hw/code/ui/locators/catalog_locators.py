from selenium.webdriver.common.by import By
from ui.locators.basic_locators import BasePageLocators


class CatalogPageLocators(BasePageLocators):
    CREATE_CATALOG_COMMON_BUTTON = (By.XPATH, "//span[contains(@class, 'vkuiButton__content') and text()='Создать каталог']")
    CANCEL_EDUCATION_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Не сейчас']")

    NEW_CATALOG_WINDOW = (By.XPATH, "//*[contains(@class, 'ModalSidebarPage_container__Zopae')]")

    FEED_OR_COMUNITY = (By.XPATH, "//*[@data-entityid='url']")
    MARKETPLACE = (By.XPATH, "//*[@data-entityid='marketplace']")
    MANUALLY = (By.XPATH, "//*[@data-entityid='file']")

    CATALOG_NAME_INPUT = (By.XPATH, f"//*[@data-testid='catalogName-input']")
    URL_INPUT = (By.XPATH, "//*[@data-testid='catalogUrl-input']")

    CREATE_CATALOG_FINISH_BUTTON = (By.XPATH, f"//*[@data-testid='submit']")

    ERROR_MESSAGE = (By.XPATH, "//*[@role='alert']")

    PERIOD_DROPDOWN = (By.XPATH, "//input[@data-testid='catalogPeriod-select']")
    CATEGORY_DROPDOWN = (By.XPATH, "//input[contains(@class, 'vkuiCustomSelectInput')]")

