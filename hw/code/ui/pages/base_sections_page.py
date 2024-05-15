from ui.pages.base_page import BasePage
from ui.locators.base_sections_page_locators import BaseSectionsPageLocators


class BaseSectionsPage(BasePage):
    locators = BaseSectionsPageLocators()

    def get_page_title(self):
        return self.find(self.locators.SUMMARY_TITLE_ADS).text
