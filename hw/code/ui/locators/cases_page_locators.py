from selenium.webdriver.common.by import By
from ui.locators.base_sections_page_locators import BaseSectionsPageLocators


class CasesPageLocators(BaseSectionsPageLocators):
    CASE_BLOCK = (By.CLASS_NAME, "Case_wrapper__JVowP")
