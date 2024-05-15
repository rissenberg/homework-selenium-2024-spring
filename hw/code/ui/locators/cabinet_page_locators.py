from selenium.webdriver.common.by import By
from ui.locators.basic_locators import BasePageLocators


class CabinetPageLocators(BasePageLocators):
    LOGO_LOCATOR = (By.CLASS_NAME, 'header_left__cv9bp')

    OVERVIEW_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/overview"]')
    CAMPAIGN_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/dashboard"]')
    AUDIENCE_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/audience"]')
    BUDGET_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/budget"]')

    EDUCATION_LOCATOR = (By.CSS_SELECTOR, '[data-testid="onboarding-button"]')
    EDUCATION_CLOSE_LOCATOR = (By.CSS_SELECTOR, '[aria-label="Закрыть"]')

    COMMERCE_CENTRE_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/ecomm/catalogs"]')
    SITES_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/pixels"]')
    APPS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/apps"]')
    LEAD_FORM_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/leadads"]')

    SETTINGS_LOCATOR = (By.CSS_SELECTOR, 'a[href="/hq/settings"]')

    HELP_LOCATOR = (By.XPATH,  "//*[contains(@class, 'Hint_hintTrigger__ixYRu sidebar_portalMenuTrigger__vwcrf')]")
    HELP_MODAL_LOCATOR = (By.CLASS_NAME, 'Tooltip_tooltipContainer__P1b-O')

    CASES_LOCATOR = (By.LINK_TEXT, "Кейсы компаний")
    SPRAVKA_LOCATOR = (By.LINK_TEXT, "Справка")
    FORUM_LOCATOR = (By.LINK_TEXT, "Форум идей")
    QUESTION_LOCATOR = (By.XPATH, f'//span[text()="Задать вопрос"]')

    BALANCE_BUTTON = (By.XPATH, "//*[contains(@class, 'balance_balance__')]")
    BALANCE_MODAL_PAGE = (By.ID, "_modal_17")

    NOTIFICATIONS_BUTTON = (By.XPATH, "//*[contains(@class, 'BellNotifications_buttonWrapper__')]")
    NOTIFICATIONS_MODAL_PAGE = (By.XPATH, "//*[contains(@class, 'BellNotificationsContent_card__')]")

    USER_AVATAR = (By.XPATH, "//*[contains(@class, 'userMenu_avatar__')]")
    USER_MENU = (By.XPATH, "//*[contains(@class, 'userMenu_menu__')]")

    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'userMenu_logoutButton__')]")
