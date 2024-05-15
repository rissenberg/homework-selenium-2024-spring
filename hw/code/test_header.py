# from base import BaseCase
# from ui.fixtures import main_page
# import pytest


# class TestHeader(BaseCase):
#     def test_go_to_home(self, main_page):
#         main_page.click_vk_ads_logo()
#         assert self.is_opened(main_page.url)

#     def test_go_to_auth(self, main_page):
#         main_page.click_nav_cabinet_button()
#         assert self.is_opened('https://id.vk.com/auth')

#     @pytest.mark.parametrize("item_name,url,open_in_new_tab", [
#         ('Новости', 'https://ads.vk.com/news', False),
#         ('Кейсы', 'https://ads.vk.com/cases', False),
#         ('Форум идей', 'https://ads.vk.com/upvote', False),
#         ('Справка', 'https://ads.vk.com/help', False),
#         ('Монетизация', 'https://ads.vk.com/partner', True)
#     ])
#     def test_go_to_sections(self, main_page, item_name, url, open_in_new_tab):
#         main_page.click_nav_item(item_name)
#         if open_in_new_tab:
#             main_page.go_to_new_tab()
#         assert self.is_opened(url)

#     def test_open_education_dropdown(self, main_page):
#         main_page.open_education_dropdown()

#         dropdown_items = [
#             'Полезные материалы',
#             'Мероприятия',
#             'Видеокурсы',
#             'Сертификация'
#         ]

#         assert main_page.education_dropdown_contain_items(dropdown_items)

#     @pytest.mark.parametrize("item_name,url,open_in_new_tab", [
#         ('Полезные материалы', 'https://ads.vk.com/insights', False),
#         ('Мероприятия', 'https://ads.vk.com/events', False),
#         ('Видеокурсы', 'https://expert.vk.com/catalog/courses/', True),
#         ('Сертификация', 'https://expert.vk.com/certification/', True)
#     ])
#     def test_go_to_dropdown_sections(self, main_page, item_name, url, open_in_new_tab):
#         main_page.open_education_dropdown()
#         main_page.click_education_dropdown_item(item_name)
#         if open_in_new_tab:
#             main_page.go_to_new_tab()
#         assert self.is_opened(url)
