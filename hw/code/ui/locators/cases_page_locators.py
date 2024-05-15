from selenium.webdriver.common.by import By
from ui.locators.base_sections_page_locators import BaseSectionsPageLocators


class CasesPageLocators(BaseSectionsPageLocators):
    CASE_ITEM = (By.XPATH, "//a[contains(@class, 'Case_wrapper__')]")
    CASE_TITLE = (By.XPATH, "//*[contains(@class, 'Case_title__')]")
