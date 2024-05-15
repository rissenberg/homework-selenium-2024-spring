# from base import BaseCase


# class TestCasesPage(BaseCase):
#     def test_title_is_displayed(self, cases_page):
#         assert cases_page.get_page_title() == 'Кейсы'

#     def test_go_to_page_of_case(self, cases_page):
#         case_title = cases_page.get_case_title()
#         cases_page.click_case_item()

#         assert self.is_opened('https://ads.vk.com/cases/')
#         assert cases_page.get_page_title() == case_title
