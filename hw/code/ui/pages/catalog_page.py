from selenium.webdriver import Keys
from ui.pages.base_page import BasePage
from ui.locators.catalog_locators import CatalogPageLocators


class CatalogPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = CatalogPageLocators()

    def click_cancel_education_button(self):
        self.click(self.locators.CANCEL_EDUCATION_BUTTON)

    def click_create_new_catalog(self):
        self.click(self.locators.CREATE_CATALOG_COMMON_BUTTON)

    def is_new_catalog_window_became_visible(self) -> bool:
        return self.is_visible(self.locators.NEW_CATALOG_WINDOW)

    def enter_catalog_name(self, catalog_name):
        input = self.find(self.locators.CATALOG_NAME_INPUT)
        input.clear()
        input.send_keys(catalog_name)

    def enter_url(self, url):
        input = self.find(self.locators.URL_INPUT)
        input.clear()
        input.send_keys(url)

    def get_error_message(self) -> str:
        return self.find(self.locators.ERROR_MESSAGE).text

    def click_feed_or_community_window(self):
        self.click(self.locators.FEED_OR_COMUNITY)

    def feed_or_community_window_became_visible(self):
        return self.is_visible(self.locators.PERIOD_DROPDOWN)

    def click_marketplace_window(self):
        self.click(self.locators.MARKETPLACE)

    def click_manually_window(self):
        self.click(self.locators.MANUALLY)

    def manually_window_became_visible(self):
        return self.is_visible(self.locators.CATEGORY_DROPDOWN)

    def click_finish_creating_catalog(self):
        self.click(self.locators.CREATE_CATALOG_FINISH_BUTTON)
        

