from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()
    url = 'https://ads.vk.com/'

    def click_vk_ads_logo(self):
        self.click(self.locators.VK_ADS_LOGO)

    def click_nav_item(self, item_name: str):
        self.click(self.locators.NAV_ITEM(item_name))

    def click_nav_cabinet_button(self):
        self.click(self.locators.NAV_CABINET_BUTTON)

    def open_education_dropdown(self):
        self.hover(self.locators.NAV_ITEM('Обучение'))

    def education_dropdown_contain_items(self, item_names: list) -> bool:
        for item_name in item_names:
            item = self.find(self.locators.NAV_EDUCATION_DROPDOWN_ITEM(item_name))
            if item is None:
                return False

        return True

    def click_education_dropdown_item(self, item_name: str):
        self.click(self.locators.NAV_EDUCATION_DROPDOWN_ITEM(item_name))

    def get_slide_title(self) -> str:
        return self.find(self.locators.SLIDER_TITLE).text

    def change_slide(self):
        self.click(self.locators.NONACTIVE_CIRCLE)

    def click_slider_cabinet_button(self):
        self.click(self.locators.SLIDER_BUTTON('/hq'))

    def click_slider_bonus_button(self):
        self.click(self.locators.SLIDER_BUTTON('/promo/firstbonus'))

    def click_see_all(self):
        self.click(self.locators.SEE_ALL_LINK)

    def click_case_item(self):
        self.click(self.locators.CASE_ITEM)

    def get_case_title(self) -> str:
        return self.find(self.locators.CASE_ITEM_TITLE).text

    def click_webinar_item(self):
        self.scroll_and_click(self.locators.WEBINAR_ITEM)
