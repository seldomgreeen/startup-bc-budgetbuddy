# BudgetBuddy

A small spending/allowance tracker you run in the terminal. Add transactions,
list them, and see your balance. This is your squad's starting product for
Elite 101 - you'll grow it one ticket at a time.

## Run it

```bash
python main.py
```

## Run the tests

```bash
python -m unittest
```

## How it's laid out

| File | What it does |
|---|---|
| `main.py` | The menu loop you interact with |
| `storage.py` | Loads and saves the JSON data file |
| `features/core.py` | The transactions, the balance, and small helpers |
| `features/reports.py` | Summary reports (half-built - finish it via a ticket) |
| `data/budgetbuddy.json` | The transaction history and starting balance |
| `tests/test_core.py` | Example tests to copy from |

## Team

<!-- Add yourself here on your Git lesson: - Your Name (role) -->

- (your squad will add themselves here)

## Where to start

Pick a ticket from the `tickets/` folder (or the Issues tab once your section
repo exists). Read `CONTRIBUTING.md` for the Definition of Done every pull
request has to meet.

## Big-expense warnings

`features.core.big_expenses(transactions, threshold)` returns expenses at or above
a positive dollar threshold, excluding income. See `tickets/ticket-01-big-expenses.md`.
This is a helper for a warning view; the terminal menu has not gained a new option.

## Average balance history

`features.reports.average_balance({"history": [...]})` returns the average
historical balance rounded to one decimal, or `0.0` for an empty history.
The finished helper from the Lesson 12 seed is included with its tests.

## Category totals

`features.reports.category_report(data)` groups every transaction by category
and totals its signed amount. Empty accounts return `{}`; refunds offset spending.
See `tickets/ticket-02-category-report.md`. Menu option 6 still shows category
counts; call this helper for dollar totals.
