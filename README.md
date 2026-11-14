# BudgetBuddy

A spending and allowance tracker you run in the terminal.

Solo founder: **Tejas Elluri**.

## Run

From the repository root, with Python 3 installed:

```bash
python3 main.py
```

The menu shows your balance, lists and adds transactions, filters by category,
and displays category counts, spending statistics, and an account summary.
Transactions are stored in `data/budgetbuddy.json`.

## Test

```bash
python3 -m unittest
```

No third-party Python packages are needed. On systems where `python` means
Python 3, it can be used instead of `python3`.

## Added helpers

- Find expenses meeting a positive dollar threshold.
- Total signed transaction amounts by category.
- Average the saved balance history, including an empty history.

These helpers are callable from Python; they do not add new menu options.
See [the product guide](docs/README.md) for examples and the solo demo plan.

## Project files

- `main.py`: terminal menu.
- `features/core.py`: transaction and spending helpers.
- `features/reports.py`: account, category-total, and history reports.
- `storage.py`: JSON loading and saving.
- `tests/`: unit tests and ticket acceptance checks.
- `tickets/`: starter task descriptions and acceptance criteria.

See [release notes](docs/RELEASE_NOTES.md) and [contributing](CONTRIBUTING.md).
