from ui.pages.base_page import BasePage
from ui.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()
    url = 'https://ads.vk.com/'

    def click_vk_ads_logo(self):
        self.click(self.locators.VK_ADS_LOGO)

    def click_nav_auth_button(self):
        self.click(self.locators.NAV_AUTH_BUTTON)

    def click_nav_news_button(self):
        self.click(self.locators.NAV_NEWS_BUTTON)

    def click_nav_case_button(self):
        self.click(self.locators.NAV_CASE_BUTTON)
        
    def click_nav_forum_button(self):
        self.click(self.locators.NAV_FORUM_BUTTON)
        
    def click_nav_partner_button(self):
        self.click(self.locators.NAV_PARTNER_BUTTON)
        
    def click_nav_help_button(self):
        self.click(self.locators.NAV_HELP_BUTTON)
        
    def click_nav_teach_button(self):
        self.click(self.locators.NAV_TEACH_BUTTON)

    def click_nav_mat_button(self):
        self.click(self.locators.NAV_MAT_BUTTON)

    def click_nav_event_button(self):
        self.click(self.locators.NAV_EVENT_BUTTON)
        
    def click_nav_sert_button(self):
        self.click(self.locators.NAV_SERT_BUTTON)
 
    def get_slide_title(self) -> str:
        return self.find(self.locators.SLIDER_TITLE).text

    def change_slide(self):
        self.click(self.locators.NONACTIVE_CIRCLE)

    def click_slider_auth_button(self):
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

    def click_more_info(self):
        self.scroll_and_click(self.locators.BUTTON_MORE_DETAILS)

    def find_text_offerContent(self):
        return self.find(self.locators.OFFER_CONTENT).text

    def find_text_summary_title(self):
        return self.find(self.locators.SUMMARY_TEXT).text
