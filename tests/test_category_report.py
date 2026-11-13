"""Acceptance checks for ticket-02: category totals."""
import unittest
from features import reports


class TestCategoryReport(unittest.TestCase):
    def test_all_transactions_are_counted_once_in_their_category(self):
        data = {"transactions": [
            {"category": "food", "amount": -5},
            {"category": "income", "amount": 20},
            {"category": "food", "amount": -2.5},
            {"category": "income", "amount": 3},
        ]}
        self.assertEqual(reports.category_report(data), {"food": -7.5, "income": 23})

    def test_empty_account_returns_empty_report(self):
        self.assertEqual(reports.category_report({"transactions": []}), {})

    def test_refund_offsets_spending_in_the_same_category(self):
        data = {"transactions": [{"category": "food", "amount": -8}, {"category": "food", "amount": 3}]}
        self.assertEqual(reports.category_report(data), {"food": -5})
