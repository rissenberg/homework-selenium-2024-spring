from base import BaseCase
from ui.fixtures import main_page
import time


class TestMainPage(BaseCase):
    
    def test_go_to_home(self, main_page):
        main_page.click_vk_ads_logo()
        assert self.is_opened(main_page.url)

    def test_go_to_auth(self, main_page):
        main_page.click_nav_auth_button()
        assert self.is_opened('https://id.vk.com/auth')

    def test_go_to_news(self, main_page):
        main_page.click_nav_news_button()
        assert self.is_opened('https://ads.vk.com/news')
        
    def test_go_to_case(self, main_page):
        main_page.click_nav_case_button()
        assert self.is_opened('https://ads.vk.com/cases')
        
    def test_go_to_forum(self, main_page):
        main_page.click_nav_forum_button()
        assert self.is_opened('https://ads.vk.com/upvote')
        
    def test_go_to_partner(self, main_page):
        main_page.click_nav_partner_button()
        main_page.go_to_new_tab()
        assert self.is_opened('https://ads.vk.com/partner')
        
    def test_go_to_help(self, main_page):
        main_page.click_nav_help_button()
        assert self.is_opened('https://ads.vk.com/help')
        
    def test_go_to_mat(self, main_page):
        main_page.click_nav_teach_button()
        main_page.click_nav_mat_button()
        assert self.is_opened('https://ads.vk.com/insights')
        
    def test_go_to_event(self, main_page):
        main_page.click_nav_teach_button()
        main_page.click_nav_event_button()
        assert self.is_opened('https://ads.vk.com/events')
        
    def test_go_to_sert(self, main_page):
        main_page.click_nav_teach_button()
        main_page.click_nav_sert_button()
        main_page.go_to_new_tab()
        assert self.is_opened('https://expert.vk.com/certification/')
    
    def test_change_slide(self, main_page):
        initial_title = main_page.get_slide_title()
        main_page.change_slide()
        assert initial_title != main_page.get_slide_title()

    def test_automatic_change_slide(self, main_page):
        initial_title = main_page.get_slide_title()
        time.sleep(7)
        assert initial_title != main_page.get_slide_title()

    def test_go_to_auth(self, main_page):
        main_page.change_slide()
        main_page.click_slider_auth_button()
        assert self.is_opened('https://id.vk.com/auth')

    def test_go_to_bonus_page(self, main_page):
        main_page.click_slider_bonus_button()
        assert self.is_opened('https://ads.vk.com/promo/firstbonus')

    def test_go_to_cases(self, main_page):
        main_page.click_see_all()
        assert self.is_opened('https://ads.vk.com/cases')

    def test_go_to_case_page(self, main_page):
        case_title = main_page.get_case_title()
        main_page.click_case_item()
        assert self.is_opened('https://ads.vk.com/cases')
        assert case_title in self.driver.page_source

    def test_go_to_webinar(self, main_page):
        main_page.click_webinar_item()
        assert self.is_opened('https://ads.vk.com/events')
