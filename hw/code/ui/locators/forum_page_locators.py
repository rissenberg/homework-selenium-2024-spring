from selenium.webdriver.common.by import By
from ui.locators.base_sections_page_locators import BaseSectionsPageLocators


class ForumsPageLocators(BaseSectionsPageLocators):
    FORUM_BLOCK = (By.CSS_SELECTOR, 'a[href="/upvote/48"]')
