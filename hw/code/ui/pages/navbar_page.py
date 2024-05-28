from ui.pages.base_page import BasePage
from ui.locators.navbar_locators import NavbarPageLocators
from ui.locators.main_page_locators import MainPageLocators

class NavbarPage(BasePage):
    locators = NavbarPageLocators()
    locators_main = MainPageLocators()
    url = 'https://ads.vk.com/'

    def click_navbar_item(self, item_text):
        self.click(self.locators.NAVBAR_HREF(item_text))
    
    def find_header(self, locator):
        return self.find(locator).text
