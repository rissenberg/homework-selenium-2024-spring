from selenium.webdriver.common.by import By
from ui.locators.base_sections_page_locators import BaseSectionsPageLocators


class EventsPageLocators(BaseSectionsPageLocators):
    EVENT_BLOCK = (By.CLASS_NAME, "Event_wrapper__AmVj3")
