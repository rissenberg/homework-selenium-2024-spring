import time

from base import BaseCase


class TestForumPage(BaseCase):
    def test_title_is_displayed(self, forum_page):
        assert forum_page.get_page_title() == 'Форум идей'

    def test_go_to_page_of_event(self, forum_page):
        forum_page.click_event_item()

        assert self.is_opened('https://ads.vk.com/upvote')
