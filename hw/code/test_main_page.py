# from base import BaseCase
# from ui.fixtures import main_page
# import time


# class TestMainPage(BaseCase):
#     def test_change_slide(self, main_page):
#         initial_title = main_page.get_slide_title()
#         main_page.change_slide()
#         assert initial_title != main_page.get_slide_title()

#     def test_automatic_change_slide(self, main_page):
#         initial_title = main_page.get_slide_title()
#         time.sleep(7)
#         assert initial_title != main_page.get_slide_title()

#     def test_go_to_auth(self, main_page):
#         main_page.change_slide()
#         main_page.click_slider_cabinet_button()
#         assert self.is_opened('https://id.vk.com/auth')

#     def test_go_to_bonus_page(self, main_page):
#         main_page.click_slider_bonus_button()
#         assert self.is_opened('https://ads.vk.com/promo/firstbonus')

#     def test_go_to_cases(self, main_page):
#         main_page.click_see_all()
#         assert self.is_opened('https://ads.vk.com/cases')

#     def test_go_to_case_page(self, main_page):
#         case_title = main_page.get_case_title()
#         main_page.click_case_item()
#         assert self.is_opened('https://ads.vk.com/cases')
#         assert case_title in self.driver.page_source

#     def test_go_to_webinar(self, main_page):
#         main_page.click_webinar_item()
#         assert self.is_opened('https://ads.vk.com/events')

