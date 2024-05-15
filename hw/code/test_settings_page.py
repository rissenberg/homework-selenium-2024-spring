import time
from base import BaseCase


class TestSettingsPage(BaseCase):
    PHONE_NUMBER = '+71234567890'
    INVALID_PHONE_NUMBER = '12345678910'
    NAME = 'AlexnadrLarin'
    INN = '526317984689'

    def test_save_button_and_cancel_button_became_visible(self, settings_page):
        settings_page.enter_phone_number(self.PHONE_NUMBER)
        assert settings_page.save_button_and_cancel_button_is_visible()

    def test_error_invalid_phone_number(self, settings_page):
        settings_page.enter_phone_number(self.INVALID_PHONE_NUMBER)
        assert settings_page.get_phone_number_error() == settings_page.ERROR_INVALID_PHONE_NUMBER

    def test_error_empty_required_fields(self, settings_page):
        settings_page.enter_phone_number(self.PHONE_NUMBER)
        assert settings_page.get_full_name_error() == settings_page.ERROR_EMPTY_REQUIRED_FIELD
        assert settings_page.get_inn_error() == settings_page.ERROR_EMPTY_REQUIRED_FIELD

    def test_add_email_input_became_visible(self, settings_page):
        settings_page.click_add_email_button()
        assert settings_page.add_email_input_is_visible()

    def test_error_too_short_inn(self, settings_page):
        settings_page.enter_inn('0')
        assert settings_page.get_inn_error() == settings_page.ERROR_TOO_SHORT_INN

    def test_error_invalid_inn(self, settings_page):
        settings_page.enter_inn('aaaaaaaaaaaa')
        assert settings_page.get_inn_error() == settings_page.ERROR_INVALID_INN

    def test_error_invalid_email(self, settings_page):
        settings_page.click_add_email_button()
        settings_page.enter_email('a')
        assert settings_page.get_email_error() == settings_page.ERROR_INVALID_EMAIL

    def test_logout_other_devices(self, settings_page):
        settings_page.click_logout_other_devices_button()
        assert settings_page.logout_devices_success_message_is_visible()

    def test_delete_cabinet_modal_page_became_visible(self, settings_page):
        settings_page.click_delete_cabinet_button()
        assert settings_page.delete_cabinet_modal_page_is_visible()
