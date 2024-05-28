from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):
    VK_ADS_LOGO = (By.CLASS_NAME, "HeaderLeft_home__EXkwQ")

    NAV_AUTH_BUTTON = (By.CLASS_NAME, "ButtonCabinet_primary__LCfol")
    NAV_NEWS_BUTTON = (By.CSS_SELECTOR, 'a[href="/news"]')
    NAV_CASE_BUTTON = (By.CSS_SELECTOR, 'a[href="/cases"]')
    NAV_FORUM_BUTTON = (By.CSS_SELECTOR, 'a[href="/upvote"]')
    NAV_PARTNER_BUTTON = (By.CSS_SELECTOR, 'a[href="/partner"]')
    NAV_HELP_BUTTON = (By.CLASS_NAME, "NavigationVKAds_help__QF364")
    NAV_TEACH_BUTTON = (By.CLASS_NAME, "NavigationVKAdsItem_item__TP0vd")
    NAV_MAT_BUTTON = (By.CLASS_NAME, "SubNavigationItem_title__HQvO0")
    NAV_EVENT_BUTTON = (By.CSS_SELECTOR, 'a[href="/events"]')
    NAV_SERT_BUTTON = (By.CSS_SELECTOR, 'a[href="https://expert.vk.com/certification/"]')


    SLIDER_TITLE = (By.CLASS_NAME, "MainSlider_active__yA0Fr")
    NONACTIVE_CIRCLE = (By.CLASS_NAME, "Bullets_center__WFrJa")

    @staticmethod
    def SLIDER_BUTTON(url):
        return By.XPATH, f"//a[contains(@class, 'MainSlider_button__') and contains(@href, '{url}')]"

    SEE_ALL_LINK = (By.CLASS_NAME, "styles_all__wnH9i")
    CASE_ITEM = (By.CLASS_NAME, "Case_content__oHhoP")
    CASE_ITEM_TITLE = (By.CLASS_NAME, "Case_title__JAisY")

    WEBINAR_ITEM = (By.CLASS_NAME, "GetStarted_wrapper__cTNLj")

    SLIDER_TITLE = (By.XPATH, "//*[contains(@class, 'MainSlider_active__')]//p")
    NONACTIVE_CIRCLE = (By.XPATH, "//*[contains(@class, 'Bullets_box__')]")
    HREF_GET_ALL_COMPANY = (By.XPATH, "//a[contains(@class, 'styles_all')]")
    DIV_ALL_COMPANY = (By.XPATH, "//div[contains(@class, 'Case_content__')]")
    CASE_TITLE = (By.XPATH, "//div[contains(@class, 'Case_title__')]")
    CASE_HREF = (By.XPATH, "//a[contains(@class, 'Case_link__')]")
    CASE_SUMMARY_TITLE = (By.XPATH, "//h1[contains(@class, 'Summary_title__')]")
    BUTTON_MORE_DETAILS = (By.XPATH, "//*[contains(@class, 'GetStarted_button__')]")
    OFFER_CONTENT = (By.XPATH, "//h1[contains(@class, 'OfferContent_title__')]")
    SUMMARY_TEXT = (By.XPATH, "//h1[contains(@class, 'Summary_title')]")