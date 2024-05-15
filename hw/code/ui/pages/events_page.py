from ui.pages.base_sections_page import BaseSectionsPage
from ui.locators.events_page_locators import EventsPageLocators


class EventsPage(BaseSectionsPage):
    locators = EventsPageLocators()
    url = 'https://ads.vk.com/events'

    def get_event_title(self) -> str:
        return self.find(self.locators.EVENT_TITLE).text

    def click_event_item(self):
        self.click(self.locators.EVENT_ITEM)
