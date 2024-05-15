from ui.pages.base_sections_page import BaseSectionsPage
from ui.locators.events_page_locators import EventsPageLocators


class EventsPage(BaseSectionsPage):
    locators = EventsPageLocators()
    url = 'https://ads.vk.com/events'

    def click_event_item(self):
        self.click(self.locators.EVENT_BLOCK)
