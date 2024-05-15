from ui.pages.base_sections_page import BaseSectionsPage
from ui.locators.news_page_locators import NewsPageLocators


class NewsPage(BaseSectionsPage):
    locators = NewsPageLocators()
    url = 'https://ads.vk.com/news'

    def click_news_item(self):
        self.click(self.locators.NEWS_BLOCK)
