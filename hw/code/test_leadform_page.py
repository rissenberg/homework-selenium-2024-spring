import time
from base import BaseCase
from ui.fixtures import lead_page
from selenium.webdriver.common.keys import Keys
import pytest

class TestLeadPage(BaseCase):
    authorize = True

    NAME_LEAD = "LEAD_FOR_TEST"
    NAME_QUESTION = "QUESTION_FOR_TEST"
    NOT_CORRECT_DATA = "FAIL"

    @pytest.mark.parametrize(
    'id',
        [
            ("0"), ("2"), ("3"), ("4"), ("5"), ("6"), ("1")
        ]
    )
    
    def test_question_create(self, lead_page):
        lead_page.skip_to_question(self.NAME_LEAD)

        lead_page.create_question(self.NAME_QUESTION)
        assert lead_page.find_title_question(self.NAME_QUESTION) == self.NAME_QUESTION

    def test_question_delete_name(self, lead_page):
        lead_page.skip_to_question(self.NAME_LEAD)

        lead_page.click_delete_first_name()
        assert lead_page.is_element_not_present(lead_page.locators.CONTACT_INFO_FIRST_NAME_DELETE)
        
    def test_question_add_contact_info(self, lead_page):
        lead_page.skip_to_question(self.NAME_LEAD)

        lead_page.add_contact_info()
        assert lead_page.find_email() != None

    def test_change_style(self, lead_page, id):
        lead_page.click_create_lead()

        lead_page.change_style(id)
        assert lead_page.find_style(id) != None

    def test_change_dark(self, lead_page):
        lead_page.click_create_lead()

        lead_page.slide_button(lead_page.locators.INPUT_LIGHT_BUTTON)
        assert lead_page.find(lead_page.locators.GET_PREVIEW_DARK) != None

    def test_change_desktop(self, lead_page):
        lead_page.click_create_lead()

        lead_page.slide_button(lead_page.locators.INPUT_MOBILE_BUTTON)
        assert lead_page.find(lead_page.locators.GET_LEAD_FROM_DESKTOP) != None

    def test_result_add_site(self, lead_page):
        lead_page.skip_to_result(self.NAME_LEAD)

        lead_page.click_add_site()
        lead_page.input_site_visible()
        assert lead_page.find_lead_site() != None

    def test_result_add_phone(self, lead_page):
        lead_page.skip_to_result(self.NAME_LEAD)

        lead_page.click_add_phone()
        lead_page.input_phone_visible()
        assert lead_page.find_lead_phone() != None

    def test_result_add_promocode(self, lead_page):
        lead_page.skip_to_result(self.NAME_LEAD)

        lead_page.click_promo()
        lead_page.input_promocode_visible()
        assert lead_page.find_lead_promocode() != None

    def test_settings_email(self, lead_page):
        lead_page.skip_to_settings(self.NAME_LEAD)

        lead_page.click_notify()
        assert lead_page.find_notify_emali_input() != None

    def test_create_lead(self, lead_page):
        lead_page.create_lead_form(self.NAME_LEAD)
        assert lead_page.find_form_in_bord(self.NAME_LEAD) != None
        lead_page.click_delete_lead_form()

    def test_search(self, lead_page):
        lead_page.create_lead_form(self.NAME_LEAD)
        in_search = lead_page.find_input_search()

        in_search.clear()
        in_search.send_keys(self.NAME_LEAD)

        assert lead_page.find_form_in_bord(self.NAME_LEAD) != None
        lead_page.click_delete_lead_form()

    def test_search_nothing(self, lead_page):
        lead_page.create_lead_form(self.NAME_LEAD)
        in_search = lead_page.find_input_search()

        in_search.clear()
        in_search.send_keys(self.NOT_CORRECT_DATA)

        assert lead_page.is_element_not_present(lead_page.locators.NAME_LINK)

        in_search.clear()
        lead_page.click_delete_lead_form()
    
    def test_edit_lead(self, lead_page):
        lead_page.create_lead_form(self.NAME_LEAD)

        lead_page.click_edit_lead()
        assert lead_page.find_modal_header() != None
        lead_page.click_close()
        lead_page.click_delete_lead_form()

    def test_delete_lead(self, lead_page):
        lead_page.create_lead_form(self.NAME_LEAD)
        lead_page.click_delete_lead_form()

        assert lead_page.is_element_not_present(lead_page.locators.NAME_LINK)