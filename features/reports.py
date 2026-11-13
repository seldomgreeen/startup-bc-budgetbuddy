"""Reporting helpers for BudgetBuddy.

Account summaries, signed category totals, and average balance history.
"""


def account_summary(data):
    return data["account_name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    """Return the signed total transaction amount for each category."""
    report = {}
    for transaction in data["transactions"]:
        category = transaction["category"]
        report[category] = report.get(category, 0) + transaction["amount"]
    return report


def average_balance(data):
    """Average of the past balances in data['history'].

    Returns a float rounded to one decimal place. An empty history returns 0.0.
    """
    history = data["history"]
    if not history:
        return 0.0
    return round(sum(history) / len(history), 1)
