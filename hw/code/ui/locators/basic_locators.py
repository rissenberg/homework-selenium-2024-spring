from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_BUTTON = (By.XPATH, "//button[contains(@class, 'CookieBanner_button__')]")
