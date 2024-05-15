from selenium.webdriver.common.by import By
from ui.locators.base_sections_page_locators import BaseSectionsPageLocators


class NewsPageLocators(BaseSectionsPageLocators):
    NEWS_BLOCK = (By.CLASS_NAME, "News_wrapper__iN3GG")
