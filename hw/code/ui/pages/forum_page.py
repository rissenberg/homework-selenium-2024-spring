from ui.pages.base_sections_page import BaseSectionsPage
from ui.locators.forum_page_locators import ForumsPageLocators


class ForumsPage(BaseSectionsPage):
    locators = ForumsPageLocators()
    url = 'https://ads.vk.com/upvote'

    def click_event_item(self):
        self.click(self.locators.FORUM_BLOCK)
