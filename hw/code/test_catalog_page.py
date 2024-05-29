from base import BaseCase

class TestCatalogPage(BaseCase):
    def test_open_new_catalog_window(self, catalog_page):
        catalog_page.click_cancel_education_button()
        catalog_page.click_create_new_catalog()
        assert catalog_page.is_new_catalog_window_became_visible()

    def test_feed_or_community_window_became_visible(self, catalog_page):
        catalog_page.click_cancel_education_button()
        catalog_page.click_create_new_catalog()
        catalog_page.click_feed_or_community_window()
        assert catalog_page.feed_or_community_window_became_visible()

    def test_feed_or_community_empty_http_error(self, catalog_page):
        catalog_page.click_cancel_education_button()
        catalog_page.click_create_new_catalog()
        catalog_page.click_feed_or_community_window()
        catalog_page.enter_url('')
        catalog_page.click_finish_creating_catalog()
        assert catalog_page.get_error_message() == catalog_page.ERROR_EMPTY_URL

    def test_feed_or_community_no_http_error(self, catalog_page):
        catalog_page.click_cancel_education_button()
        catalog_page.click_create_new_catalog()
        catalog_page.click_feed_or_community_window()
        catalog_page.enter_url('1')
        catalog_page.click_finish_creating_catalog()
        assert catalog_page.get_error_message() == catalog_page.ERROR_NO_HTTP

    def test_feed_or_community_incorrect_url_error(self, catalog_page):
        catalog_page.click_cancel_education_button()
        catalog_page.click_create_new_catalog()
        catalog_page.click_feed_or_community_window()
        catalog_page.enter_url('https://afasdfdas')
        catalog_page.click_finish_creating_catalog()
        assert catalog_page.get_error_message() == catalog_page.ERROR_INVALID_URL


    def  test_open_marketplace_window(self, catalog_page):
        catalog_page.click_cancel_education_button()
        catalog_page.click_create_new_catalog()
        catalog_page.click_marketplace_window()
        catalog_page.enter_url('https://afasdfdas')
        catalog_page.click_finish_creating_catalog()
        assert catalog_page.get_error_message() == catalog_page.ERROR_NOT_REAL_MARKET


    def test_manually_window_became_visible(self, catalog_page):
        catalog_page.click_cancel_education_button()
        catalog_page.click_create_new_catalog()
        catalog_page.click_manually_window()
        assert catalog_page.manually_window_became_visible()
