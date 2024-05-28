from ui.locators.lead_page_locators import LeadPageLocators
from ui.pages.base_page import BasePage
import time
from selenium.webdriver.common.keys import Keys

class LeadPage(BasePage):
    locators = LeadPageLocators()
    url = 'https://ads.vk.com/hq/leadads/leadforms'
    
    def click_continue(self):
        self.click(self.locators.BUTTON_CONTINUE)

    def decor_part(self, name_lead):
        self.DOWNLOAD_AVATAR()
        in_name_lead = self.find(self.locators.INPUT_NAME_LEAD_FORM)

        in_name_lead.clear()
        in_name_lead.send_keys(name_lead)

        in_name_company = self.find(self.locators.INPUT_NAME_COMPANY)
        in_name_company.send_keys(name_lead)

        in_title = self.find(self.locators.INPUT_TITLE)
        in_title.send_keys(name_lead)

        in_description = self.find(self.locators.INPUT_DESCRIPTION)
        in_description.send_keys(name_lead)
        self.find_replace()
        self.click_continue()
        
    def click_create_lead(self):
        self.click(self.locators.MAIN_BUTTON)

    def DOWNLOAD_AVATAR(self):
        self.click(self.locators.DOWNLOAD_AVATAR)
        self.click(self.locators.GET_AVATAR)
    
    def find_replace(self):
        return self.find(self.locators.CHANGE_AVATAR, 7)
    
    def change_style(self, item):
        self.click(self.locators.BUTTON_STYLE(item))

    def find_style(self, item):
        return self.find(self.locators.CHECK_STYLE(item))
    
    def slide_button(self, locator):
        input = self.find(locator)
        input.send_keys(Keys.RIGHT)

    def create_lead_form(self, name_lead):
        self.click_create_lead()
        self.decor_part(name_lead)
        self.click_continue()
        self.click_continue()
        in_last_name = self.find(self.locators.INPUT_LAST_NAME)
        in_last_name.send_keys(name_lead)
        in_last_name = self.find(self.locators.INPUT_ADDRESS)
        in_last_name.send_keys(name_lead)
        self.click_continue()


    def add_contact_info(self):
        self.click(self.locators.BUTTON_ADD_CONTACT)
        self.click(self.locators.CHECKBOX_EMAIL)
        self.click(self.locators.ADD_BUTTON_CONTACT_INFO)

    def find_email(self):
        return self.find(self.locators.FIND_EMAIL_CONTACT_INFO)
    
    def click_delete_first_name(self):
        self.click(self.locators.CONTACT_INFO_FIRST_NAME_DELETE)

    def create_question(self, question_name):
        self.click(self.locators.BUTTON_ADD_QUESTION)
        textarea_question = self.find(self.locators.QUESTION_TEXTAREA)
        textarea_question.send_keys(question_name)

    def find_title_question(self, question_name):
        return self.find(self.locators.TITLE_QUESTION(question_name)).text

    def click_add_site(self):
        self.click(self.locators.BUTTON_ADD_SITE)

    def click_add_phone(self):
        self.click(self.locators.BUTTON_ADD_PHONE)
    
    def click_promo(self):
        self.click(self.locators.BUTTON_ADD_PROMO_CODE)
    
    def input_site_visible(self):
        self.find(self.locators.INPUT_SITE).send_keys("example.com")
    
    def input_phone_visible(self):
        self.find(self.locators.INPUT_PHONE).send_keys("99999")
    
    def input_promocode_visible(self):
        self.find(self.locators.INPUT_PROMOCODE).send_keys("a")
    
    def find_lead_phone(self):
        return self.find(self.locators.LEAD_PHONE).text
    
    def find_lead_site(self):
        return self.find(self.locators.LEAD_SITE).text
    
    def find_lead_promocode(self):
        return self.find(self.locators.LEAD_PROMOCODE)
    
    def click_notify(self):
        self.click(self.locators.NOTIFY_CHECKBOX_EMAIL)
    
    def find_notify_emali_input(self):
        return self.find(self.locators.NOTIFY_EMAIL)
    
    def find_form_in_bord(self, name_link):
        return self.find(self.locators.NAME_LINK(name_link))
    
    def click_delete_lead_form(self):
        self.scroll_and_click(self.locators.BUTTON_DELETE)
        self.click(self.locators.FINALLY_DELETE)
    
    def click_edit_lead(self):
        self.scroll_and_click(self.locators.BUTTON_EDIT)
    
    def find_modal_header(self):
        return self.find(self.locators.MODAL_HEADER_EDIT)
    
    def find_input_search(self):
        return self.find(self.locators.INPUT_SEARCH)
    
    def skip_to_question(self, name_lead):
        self.click_create_lead()
        self.decor_part(name_lead)        

    def skip_to_result(self, name_lead):
        self.click_create_lead()
        self.decor_part(name_lead)
        self.click_continue()
    
    def skip_to_settings(self, name_lead):
        self.click_create_lead()
        self.decor_part(name_lead)
        self.click_continue()
        self.click_continue()
    
    def click_close(self):
        self.click(self.locators.BUTTON_CANCEL)
