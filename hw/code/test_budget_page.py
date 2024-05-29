import pytest
from base import BaseCase

@pytest.fixture
def replenishment_window(budget_page):
    budget_page.click_replenish_budget_button()

class TestBudgetPage(BaseCase):
    def test_open_replenishment_window(self, replenishment_window, budget_page):
        assert budget_page.replenishment_window_is_visible()

    def test_error_too_little_sum(self, replenishment_window, budget_page):
        budget_page.enter_sum(1)
        budget_page.click_submit_button()
        assert budget_page.get_error_message() == budget_page.ERROR_TOO_LITTLE_SUM

    def test_enter_non_numeric_sum(self, replenishment_window, budget_page):
        budget_page.enter_sum('a')
        assert budget_page.get_sum_value() == ''

    def test_enter_non_numeric_sum_without_vat(self, replenishment_window, budget_page):
        budget_page.enter_sum_without_vat('a')
        assert budget_page.get_sum_without_vat_value() == ''

    def test_vat(self, replenishment_window, budget_page):
        budget_page.enter_sum(600)
        assert budget_page.get_sum_without_vat_value() == '500 ₽'

    def test_open_vkpay(self, replenishment_window, budget_page):
        budget_page.enter_sum(budget_page.MIN_SUM)
        budget_page.click_submit_button()
        assert budget_page.pay_window_is_visible()
