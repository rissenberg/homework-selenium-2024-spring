from selenium.webdriver.common.by import By

class NavbarPageLocators:
    @staticmethod
    def NAVBAR_HREF(item_text):
        return By.XPATH, f"//*[contains(@class, 'NavigationVKAdsItem_link__') and text()='{item_text}']"
