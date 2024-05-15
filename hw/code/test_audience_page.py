import pytest
from datetime import datetime
from base import BaseCase

AUDIENCE_NAME = 'Обеспечение качества ' + datetime.now().strftime('%d-%m-%Y')
SOURCE_NAME = 'Ключевые фразы'
KEY_PHRASE = 'vk-qa'


@pytest.fixture
def create_audience_modal_page(audience_page):
    audience_page.click_create_audience_button()


@pytest.fixture
def key_phrases_source(create_audience_modal_page, audience_page):
    audience_page.click_add_source_button()
    audience_page.select_source(SOURCE_NAME)
    audience_page.enter_key_phrases(KEY_PHRASE)
    audience_page.click_modal_page_submit_button()


class TestAudiencePage(BaseCase):
    def test_create_audience_modal_is_visible(self, create_audience_modal_page, audience_page):
        assert audience_page.create_audience_modal_page_is_visible()

    def test_default_audience_name(self, create_audience_modal_page, audience_page):
        assert audience_page.get_default_audience_name() == audience_page.DEFAULT_AUDIENCE_NAME

    def test_create_audience(self, key_phrases_source, audience_page):
        audience_page.enter_audience_name(AUDIENCE_NAME)
        audience_page.click_modal_page_submit_button()
        assert audience_page.get_created_audience_title() == AUDIENCE_NAME

    def test_error_long_audience_name(self, create_audience_modal_page, audience_page):
        audience_page.enter_audience_name('1' * (audience_page.MAX_LENGTH_OF_NAME + 1))
        assert audience_page.get_error() == audience_page.ERROR_TOO_LONG_NAME

    def test_add_source_modal_is_visible(self, create_audience_modal_page, audience_page):
        audience_page.click_add_source_button()
        assert audience_page.add_source_modal_page_is_visible()

    def test_add_key_phrase(self, key_phrases_source, audience_page):
        source_card_content = audience_page.get_source_card_content()
        assert KEY_PHRASE in source_card_content
