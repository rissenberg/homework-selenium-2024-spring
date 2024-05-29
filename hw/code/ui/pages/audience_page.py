from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from ui.pages.base_page import BasePage
from ui.locators.audience_page_locators import AudiencePageLocators
from datetime import datetime
import time


class AudiencePage(BasePage):
    url = 'https://ads.vk.com/hq/audience'
    locators = AudiencePageLocators()

    DEFAULT_AUDIENCE_NAME = 'Аудитория ' + datetime.now().strftime('%Y-%m-%d')
    ERROR_TOO_LONG_NAME = 'Максимальная длина 255 символов'
    MAX_LENGTH_OF_NAME = 255

    def click_create_audience_button(self):
        create_button = self.wait_until(EC.visibility_of_element_located(self.locators.CREATE_AUDIENCE_BUTTON), 10)
        create_button.click()

    def create_audience_modal_page_is_visible(self) -> bool:
        return self.is_visible(self.locators.CREATE_AUDIENCE_MODAL_PAGE)

    def get_default_audience_name(self):
        return self.find(self.locators.AUDIENCE_NAME_INPUT).get_attribute('value')

    def enter_audience_name(self, audience_name: str):
        elem = self.find(self.locators.AUDIENCE_NAME_INPUT)
        elem.clear()
        elem.send_keys(audience_name)
        elem.send_keys(Keys.ENTER)

    def get_error(self) -> str:
        return self.find(self.locators.ERROR).text

    def click_add_source_button(self):
        self.click(self.locators.ADD_SOURCE_BUTTON)

    def add_source_modal_page_is_visible(self) -> bool:
        return self.is_visible(self.locators.ADD_SOURCE_MODAL_PAGE)

    def select_source(self, source_name):
        time.sleep(1)
        source_item = self.wait_until(EC.visibility_of_element_located(self.locators.SOURCE_ITEM(source_name)), 10)
        source_item.click()

    def get_source_card_content(self) -> str:
        return self.find(self.locators.SOURCE_CARD_CONTENT).text

    def get_created_audience_title(self) -> str:
        return self.find(self.locators.CREATED_AUDIENCE_TITLE).text

    def enter_key_phrases(self, key_phrase):
        key_phrases_input = self.find(self.locators.KEY_PHRASES_INPUT)
        key_phrases_input.clear()
        key_phrases_input.send_keys(key_phrase)

    def click_modal_page_submit_button(self):
        elem = self.wait_until(EC.visibility_of_element_located(self.locators.MODAL_PAGE_SUBMIT_BUTTON), 10)
        elem.click()

    def click_delete_audience_button(self):
        delete_button = self.wait_until(EC.visibility_of_element_located(self.locators.DELETE_AUDIENCE_BUTTON), 10)
        delete_button.click()
        delete_confirm_button = self.wait_until(EC.visibility_of_element_located(self.locators.DELETE_CONFIRM_BUTTON), 10)
        delete_confirm_button.click()

    def click_edit_audience_button(self):
        edit_button = self.wait_until(EC.visibility_of_element_located(self.locators.EDIT_AUDIENCE_BUTTON), 10)
        edit_button.click()
