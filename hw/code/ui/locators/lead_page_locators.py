from selenium.webdriver.common.by import By
from ui.locators.basic_locators import BasePageLocators


class LeadPageLocators(BasePageLocators):
    MAIN_BUTTON = (By.CLASS_NAME, "vkuiButton__content")
    DOWNLOAD_AVATAR = (By.CLASS_NAME, "vkuiSimpleCell__middle")
    GET_AVATAR = (By.CLASS_NAME, "ImageItems_image__Zq8Np")
    CHANGE_AVATAR = (By.CLASS_NAME, "vkuiButton__in")
    GET_PREVIEW_LIGHT = (By.CLASS_NAME, "vkuiIcon--sun_outline_20")
    GET_PREVIEW_DARK = (By.CLASS_NAME, "vkuiIcon--moon_outline_20")
    GET_LEAD_FROM_DESKTOP = (By.CLASS_NAME, "CreateLeadFormModal_desktop__")
    INPUT_LIGHT_BUTTON = (By.XPATH, '//input[@value="light"]')
    INPUT_DARK_BUTTON = (By.XPATH, '//input[@value="dark"]')
    INPUT_MOBILE_BUTTON = (By.XPATH, '//input[@value="mobile"]')
    INPUT_NAME_LEAD_FORM = (By.XPATH, '//input[@placeholder="Название лид-формы"]')
    INPUT_NAME_COMPANY = (By.XPATH, '//input[@placeholder="Название компании"]')
    INPUT_TITLE = (By.XPATH, '//input[@placeholder="Текст заголовка"]')
    INPUT_DESCRIPTION = (By.XPATH, '//input[@placeholder="Краткое описание опроса"]') 
    BUTTON_CONTINUE = (By.XPATH, '//button[@data-testid="submit"]')
    BUTTON_CANCEL = (By.XPATH, '//button[@data-testid="cancel"]')
    BUTTON_ADD_CONTACT = (By.CLASS_NAME, "Questions_addContactFieldsBtn__")
    CHECKBOX_EMAIL = (By.XPATH, '//div[contains(@class, "AddContactsFieldsModal_checklist__")]//label[2]')
    ADD_BUTTON_CONTACT_INFO = (By.XPATH, '//div[contains(@class, "ModalManagerPage_footer__")]//button')
    FIND_EMAIL_CONTACT_INFO = (By.XPATH, '//input[@placeholder="Введите email"]')
    BUTTON_ADD_QUESTION = (By.XPATH, '//button[.//span[text()="Добавить вопрос"]]')
    QUESTION_TEXTAREA = (By.CLASS_NAME, "vkuiTextarea__")
    CONTACT_INFO_FIRST_NAME_DELETE = (By.XPATH, '//button[@aria-label="Delete" and @data-id="first_name"]')
    BUTTON_ADD_SITE = (By.XPATH, '//div[@data-testid="add-site-btn"]') 
    BUTTON_ADD_PHONE = (By.XPATH, '//div[@data-testid="add-phone-btn"]')
    BUTTON_ADD_PROMO_CODE = (By.XPATH, '//div[@data-testid="add-promo-code-btn"]')
    INPUT_SITE = (By.XPATH, '//div[@placeholder="Введите ссылку на сайт"]//span//input')
    INPUT_PHONE = (By.XPATH, '//input[@placeholder="+7......"]')
    INPUT_PROMOCODE = (By.XPATH, '//input[@placeholder="Введите промокод"]')
    LEAD_PHONE = (By.XPATH, '//a[contains(@href,"tel:")]')
    LEAD_SITE = (By.XPATH, '//a[@rel="noreferrer noopener"]')
    LEAD_PROMOCODE = (By.XPATH, '//button[@aria-label="Скопировать"]')
    NOTIFY_CHECKBOX_EMAIL = (By.CLASS_NAME, "vkuiCheckbox__icon--off")
    NOTIFY_EMAIL = (By.XPATH, '//input[@placeholder="email@example.com"]')
    INPUT_LAST_NAME = (By.XPATH, '//input[@placeholder="Введите фамилию, имя и отчество"]')
    INPUT_ADDRESS = (By.XPATH, '//input[@placeholder="Введите адрес"]')
    INPUT_SEARCH = (By.XPATH, '//input[@data-testid="search"]')
    BUTTON_DELETE = (By.XPATH, '//div[contains(@class, "Nav_list")]//button[2]')
    FINALLY_DELETE = (By.XPATH, '//button[@data-testid="submit"]')
    BUTTON_EDIT = (By.XPATH, '//div[contains(@class, "Nav_list")]//button[1]')
    MODAL_HEADER_EDIT = (By.CLASS_NAME, "ModalSidebarPage_title__")
    INPUT_DROP_DOWN = (By.XPATH, '//input[@aria-haspopup="listbox"]')
    @staticmethod
    def BUTTON_STYLE(style_id):
        return By.XPATH, f"//div[@data-id='{style_id}']"
    @staticmethod
    def CHECK_STYLE(gradient_style):
        return By.XPATH, f"//div[contains(@class, LeadForm-module_gradient{gradient_style})]"
    @staticmethod
    def NAME_LINK(name):
        return By.XPATH, f"//button[contains(@class, 'NameCell_link__') and text()='{name}']"
    @staticmethod
    def TITLE_QUESTION(question_name):
        return By.XPATH, f"//h3[text()='{question_name}']"
