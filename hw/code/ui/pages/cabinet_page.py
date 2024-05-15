from ui.pages.base_page import BasePage
from ui.locators.cabinet_page_locators import CabinetPageLocators


class CabinetPage(BasePage):
    url = 'https://ads.vk.com/hq/overview'
    locators = CabinetPageLocators()

    def click_campaign(self):
        self.click(self.locators.CAMPAIGN_LOCATOR)

    def click_audience(self):
        self.click(self.locators.AUDIENCE_LOCATOR)

    def click_budget(self):
        self.click(self.locators.BUDGET_LOCATOR)

    def click_education(self):
        self.click(self.locators.EDUCATION_LOCATOR)

    def is_education_modal_shown(self):
        return self.is_visible(self.locators.EDUCATION_MODAL_LOCATOR)

    def click_cross_education_modal(self):
        self.click(self.locators.EDUCATION_MODAL_CROSS_LOCATOR)

    def is_education_modal_closed(self):
        return self.is_not_visible(self.locators.EDUCATION_MODAL_LOCATOR)

    def click_commerce_centre(self):
        self.click(self.locators.COMMERCE_CENTRE_LOCATOR)

    def click_sites(self):
        self.click(self.locators.SITES_LOCATOR)

    def click_apps(self):
        self.click(self.locators.APPS_LOCATOR)

    def click_lead_forms(self):
        self.click(self.locators.LEAD_FORM_LOCATOR)

    def click_settings(self):
        self.click(self.locators.SETTINGS_LOCATOR)

    def click_help(self):
        self.scroll_click(self.locators.HELP_LOCATOR)

    def is_help_modal_shown(self):
        return self.is_visible(self.locators.HELP_MODAL_LOCATOR)

    def is_help_modal_closed(self):
        return self.is_not_visible(self.locators.HELP_MODAL_LOCATOR)

    def click_cases(self):
        self.click(self.locators.CASES_LOCATOR)

    def click_spravka(self):
        self.click(self.locators.SPRAVKA_LOCATOR)

    def click_forum(self):
        self.click(self.locators.FORUM_LOCATOR)

    def click_question(self):
        self.click(self.locators.QUESTION_LOCATOR)

    def click_balance_button(self):
        self.click(self.locators.BALANCE_BUTTON)

    def click_notifications_button(self):
        self.click(self.locators.NOTIFICATIONS_BUTTON)

    def notifications_modal_page_became_visible(self) -> bool:
        return self.become_visible(self.locators.NOTIFICATIONS_MODAL_PAGE)

    def click_user_avatar(self):
        self.click(self.locators.USER_AVATAR)

    def user_menu_became_visible(self) -> bool:
        return self.become_visible(self.locators.USER_MENU)

    def click_logout_button(self):
        self.click(self.locators.LOGOUT_BUTTON)
