"""Acceptance checks for ticket-01: big-expenses warnings."""
import unittest
from features import core


class TestBigExpenses(unittest.TestCase):
    def test_only_large_expenses_including_threshold_are_returned(self):
        txns = [{"amount": -12.5}, {"amount": 30}, {"amount": -9.99}, {"amount": -10}]
        self.assertEqual(core.big_expenses(txns, 10), [txns[0], txns[3]])

    def test_no_qualifying_expenses_and_empty_input(self):
        self.assertEqual(core.big_expenses([{"amount": 20}, {"amount": -2}], 10), [])
        self.assertEqual(core.big_expenses([], 10), [])

    def test_threshold_must_be_positive(self):
        for threshold in (0, -5):
            with self.subTest(threshold=threshold), self.assertRaises(ValueError):
                core.big_expenses([], threshold)
