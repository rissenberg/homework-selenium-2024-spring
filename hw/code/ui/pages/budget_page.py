from ui.pages.base_page import BasePage
from ui.locators.budget_page_locators import BudgetPageLocators


class BudgetPage(BasePage):
    url = 'https://ads.vk.com/hq/budget/transactions'
    locators = BudgetPageLocators()

    MIN_SUM = 600
    MIN_SUM_WITHOUT_VAT = 500

    ERROR_TOO_LITTLE_SUM = 'Минимальная сумма 600,00 ₽'

    def click_replenish_budget_button(self):
        self.click(self.locators.REPLENISH_BUDGET_BUTTON)

    def replenishment_window_is_visible(self) -> bool:
        return self.is_visible(self.locators.REPLENISHMENT_WINDOW)

    def enter_sum(self, sum: str | int):
        sum_input = self.find(self.locators.SUM_INPUT)
        sum_input.clear()
        sum_input.send_keys(sum)

    def get_sum_value(self) -> str | None:
        return self.find(self.locators.SUM_INPUT).get_attribute('value')

    def enter_sum_without_vat(self, sum: str | int):
        sum_without_vat_input = self.find(self.locators.SUM_WITHOUT_VAT_INPUT)
        sum_without_vat_input.clear()
        sum_without_vat_input.send_keys(sum)

    def get_sum_without_vat_value(self) -> str | None:
        return self.find(self.locators.SUM_WITHOUT_VAT_INPUT).get_attribute('value')
    
    def click_submit_button(self):
        self.click(self.locators.SUBMIT_BUTTON)

    def get_error_message(self) -> str:
        return self.find(self.locators.ERROR_ALERT).text

    def pay_window_is_visible(self) -> bool:
        return self.is_visible(self.locators.PAY_WINDOW)
