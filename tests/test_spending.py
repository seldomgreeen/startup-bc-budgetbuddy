"""Solo-founder follow-up: an uncovered core function."""
import unittest
from features import core


class TestTotalSpent(unittest.TestCase):
    def test_expenses_are_positive_and_income_is_ignored(self):
        rows = [{"amount": -2.5}, {"amount": 20}, {"amount": -7}]
        self.assertEqual(core.total_spent(rows), 9.5)

    def test_empty_transactions_have_no_spending(self):
        self.assertEqual(core.total_spent([]), 0.0)
