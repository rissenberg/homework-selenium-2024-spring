from selenium.webdriver.common.by import By
from ui.locators.basic_locators import BasePageLocators


class CampaignsPageLocators(BasePageLocators):
    SKIP_HELP_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Попробовать позже']")
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Создать кампанию']")
    CONTINUE_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Продолжить']")

    SITE = (By.XPATH, "//*[@data-id='site_conversions']")
    SITE_INPUT = (By.XPATH, "//*[@placeholder='Введите ссылку на сайт']")

    ERROR = (By.XPATH, "//*[@role='alert']/div")

    GOAL_DROPDOWN = (By.XPATH, "//*[@data-testid='priced-goal']")
    STRATEGY_DROPDOWN = (By.XPATH, "//*[@data-testid='autobidding-mode']")
    BUDGET_INPUT = (By.XPATH, "//*[contains(@class, 'Budget_input__')]/input")

    DATES = (By.XPATH, "//*[contains(@class, 'Dates_layout__')]")
    START_DATE = (By.XPATH, "//*[contains(@class, 'Dates_datepickerStart__')]/input")

    @staticmethod
    def ACTIVE_STAGE(stage_name):
        return By.XPATH, f"//*[contains(@class, 'Steps_step_active__') and child::span[text()='{stage_name}']]"

    REGION_QUICK_SELECTION = (By.XPATH, "//*[contains(@class, 'RegionsQuickSelection_item__')]")

    MEDIA_BUTTON = (By.XPATH, "//*[contains(@class, 'UploadMediaButton_buttonLogoContent__')]")
    PANEL_TITLE = (By.XPATH, "//*[contains(@class, 'ModalSidebarPage_title')]")
    GENERATED_IMAGES_TAB = (By.ID, "tab-media-library-photobank")
    IMAGE_ITEM = (By.XPATH, "//*[contains(@class, 'ImageItems_image__')]")
    SELECTED_IMAGE = (By.XPATH, "//*[contains(@class, 'AdMediaPreview_loaded__')]")

    TITLE = (By.XPATH, "//*[contains(@class, 'TextRole_textFieldWrap__')]//input")
    DESCRIPTION = (By.XPATH, "//*[contains(@class, 'TextRole_textFieldWrap__')]//textarea")

    PREVIEW_TITLE = (By.XPATH, "//*[contains(@class, 'preview_preview__')]//h3[contains(@class, 'Header_name__')]")
    PREVIEW_DESCRIPTION = (By.XPATH, "//*[contains(@class, 'preview_preview__')]//*[contains(@class, 'Default_text__')]")

    PUBLISH_BUTTON = (By.XPATH, "//*[contains(@class, 'vkuiButton__content') and text()='Опубликовать']")
