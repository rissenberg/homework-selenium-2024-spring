from ui.pages.base_sections_page import BaseSectionsPage
from ui.locators.cases_page_locators import CasesPageLocators


class CasesPage(BaseSectionsPage):
    locators = CasesPageLocators()
    url = 'https://ads.vk.com/cases'

    def click_case_item(self):
        self.click(self.locators.CASE_BLOCK)
