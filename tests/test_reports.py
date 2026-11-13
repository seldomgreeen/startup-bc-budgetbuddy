"""Lesson 12 tests for the finished average-balance report."""
import unittest
from features import reports


class TestAverageBalance(unittest.TestCase):
    def test_history_is_averaged_and_rounded_to_one_decimal(self):
        self.assertEqual(reports.average_balance({"history": [10.0, 20.0, 25.0]}), 18.3)

    def test_empty_history_returns_zero(self):
        self.assertEqual(reports.average_balance({"history": []}), 0.0)
