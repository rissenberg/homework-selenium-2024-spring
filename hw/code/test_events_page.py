import time

from base import BaseCase


class TestEventsPage(BaseCase):
    def test_title_is_displayed(self, events_page):
        assert events_page.get_page_title() == 'Мероприятия'

    def test_go_to_page_of_event(self, events_page):
        events_page.click_event_item()

        assert self.is_opened('https://ads.vk.com/events/')
