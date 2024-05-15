from datetime import datetime
import pytest
from base import BaseCase

SITE_URL = 'https://formhub.site'
TITLE = 'Formhub Service'
DESCRIPTION = 'Create, Share and Analyse forms using professional tools'


@pytest.fixture
def new_campaign(campaigns_page):
    campaigns_page.skip_help()
    campaigns_page.click_create_campaign()


@pytest.fixture
def enter_site(new_campaign, campaigns_page):
    campaigns_page.select_site()
    campaigns_page.enter_site_url(SITE_URL)


@pytest.fixture
def second_stage(enter_site, campaigns_page):
    campaigns_page.enter_budget_amount(campaigns_page.MIN_BUDGET)
    campaigns_page.click_continue_button()


@pytest.fixture
def third_stage(second_stage, campaigns_page):
    campaigns_page.select_regions()
    campaigns_page.click_continue_button()


class TestCampaignsPage(BaseCase):
    def test_open_new_campaign(self, new_campaign):
        assert self.is_opened('https://ads.vk.com/hq/new_create/ad_plan')

    def test_site_input_is_visible(self, new_campaign, campaigns_page):
        campaigns_page.select_site()
        assert campaigns_page.site_input_is_visible()

    def test_error_empty_site_field(self, new_campaign, campaigns_page):
        campaigns_page.select_site()
        campaigns_page.click_continue_button()
        assert campaigns_page.get_error() == campaigns_page.ERROR_EMPTY_FIELD

    def test_additional_options_is_visible(self, enter_site, campaigns_page):
        assert campaigns_page.options_is_visible()

    def test_check_date(self, enter_site, campaigns_page):
        assert campaigns_page.get_start_date() == datetime.now().strftime('%d.%m.%Y')

    def test_error_empty_budget_field(self, enter_site, campaigns_page):
        campaigns_page.click_continue_button()
        assert campaigns_page.get_error() == campaigns_page.ERROR_EMPTY_FIELD

    def test_error_small_budget_field(self, enter_site, campaigns_page):
        campaigns_page.enter_budget_amount(campaigns_page.MIN_BUDGET - 1)
        campaigns_page.click_continue_button()
        assert campaigns_page.get_error() == campaigns_page.ERROR_TOO_SMALL_BUDGET

    def test_open_second_stage(self, second_stage, campaigns_page):  #
        assert campaigns_page.is_active_stage(campaigns_page.SECOND_STAGE_NAME)

    def test_open_third_stage(self, third_stage, campaigns_page):
        assert campaigns_page.is_active_stage(campaigns_page.THIRD_STAGE_NAME)

    def test_open_media_browser(self, third_stage, campaigns_page):
        campaigns_page.click_media_button()
        assert campaigns_page.get_panel_title() == 'Медиатека'

    def test_check_preview(self, third_stage, campaigns_page):
        campaigns_page.enter_title_and_description(TITLE, DESCRIPTION)
        assert campaigns_page.get_preview_title() == TITLE
        assert campaigns_page.get_preview_description() == DESCRIPTION
