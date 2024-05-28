from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class BaseSectionsPageLocators(BasePageLocators):
    SUMMARY_TITLE_ADS = (By.CSS_SELECTOR, 'h1[data-test-id="summary-title-ads"]')
