import time
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.locators.campaigns_page_locators import CampaignsPageLocators


class CampaignsPage(BasePage):
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'
    locators = CampaignsPageLocators()

    MIN_BUDGET = 100
    ERROR_EMPTY_FIELD = 'Обязательное поле'
    ERROR_TOO_SMALL_BUDGET = 'Бюджет кампании должен быть не меньше 100₽'
    SECOND_STAGE_NAME = 'Группы объявлений'
    THIRD_STAGE_NAME = 'Объявления'

    def skip_help(self):
        try:
            self.click(self.locators.SKIP_HELP_BUTTON)
        except TimeoutException:
            pass

    def click_create_campaign(self):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON)

    def select_site(self):
        self.click(self.locators.SITE)

    def site_input_is_visible(self) -> bool:
        return self.is_visible(self.locators.SITE_INPUT)

    def get_error(self) -> str:
        return self.find(self.locators.ERROR).text

    def click_continue_button(self):
        wait = self.wait(10)
        continue_button = wait.until(EC.visibility_of_element_located(self.locators.CONTINUE_BUTTON))
        continue_button.click()

    def enter_site_url(self, url: str):
        elem = self.find(self.locators.SITE_INPUT)
        elem.clear()
        elem.send_keys(url)
        elem.send_keys(Keys.ENTER)

    def options_is_visible(self) -> bool:
        return (self.is_visible(self.locators.GOAL_DROPDOWN)
                and self.is_visible(self.locators.STRATEGY_DROPDOWN)
                and self.is_visible(self.locators.BUDGET_INPUT)
                and self.is_visible(self.locators.DATES))

    def get_start_date(self) -> str | None:
        return self.find(self.locators.START_DATE).get_attribute('value')

    def enter_budget_amount(self, amount: str | int):
        elem = self.find(self.locators.BUDGET_INPUT)
        elem.clear()
        elem.send_keys(amount)
        time.sleep(1)

    def is_active_stage(self, stage_name: str):
        try:
            self.find(self.locators.ACTIVE_STAGE(stage_name))
            return True
        except TimeoutException:
            return False

    def select_regions(self):
        wait = self.wait(10)
        region_selection = wait.until(EC.visibility_of_element_located(self.locators.REGION_QUICK_SELECTION))
        region_selection.click()

    def get_panel_title(self) -> str:
        return self.find(self.locators.PANEL_TITLE).text

    def click_media_button(self):
        self.click(self.locators.MEDIA_BUTTON)

    def select_image(self):
        self.click(self.locators.GENERATED_IMAGES_TAB)
        self.click(self.locators.IMAGE_ITEM)

    def is_image_selected(self) -> bool:
        try:
            self.find(self.locators.SELECTED_IMAGE)
            return True
        except TimeoutException:
            return False

    def enter_title_and_description(self, title: str, description: str):
        elem = self.find(self.locators.TITLE)
        elem.clear()
        elem.send_keys(title)

        elem = self.find(self.locators.DESCRIPTION)
        elem.clear()
        elem.send_keys(description)

    def get_preview_title(self) -> str:
        return self.find(self.locators.PREVIEW_TITLE).text

    def get_preview_description(self) -> str:
        return self.find(self.locators.PREVIEW_DESCRIPTION).text

    def click_publish_button(self):
        self.click(self.locators.PUBLISH_BUTTON)
