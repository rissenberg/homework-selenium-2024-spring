from selenium.webdriver.common.by import By
from ui.locators.base_sections_page_locators import BaseSectionsPageLocators


class EventsPageLocators(BaseSectionsPageLocators):
    EVENT_ITEM = (By.XPATH, "//a[contains(@class, 'Event_wrapper__')]")
    EVENT_TITLE = (By.XPATH, "//*[contains(@class, 'Event_title__')]")
