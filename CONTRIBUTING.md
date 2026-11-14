# Contributing

This is Tejas Elluri's solo BudgetBuddy project. Keep each change on a
descriptive branch and review its diff before integrating it into `main`.

## Definition of Done

- Reference the task's file in `tickets/`, or identify the lesson task.
- Run the application or affected helper and confirm its expected behavior.
- Review the diff for correctness, task coverage, and readability. A solo
  self-review replaces a teammate review.
- Run `python3 -m unittest` and retain the passing output with the work log.
- Update the product guide or release notes to match the behavior shipped.

## Branches

Use `tejas/<short-description>` for personal work and `release/v1.0` for
this release. Make commits on the work branch, then integrate tested,
reviewed product changes into `main` with a fast-forward merge.

Seeded debugging exercises stay on their personal fix branches. Preserve
the `lesson/*-start` branches so the original bugs can still be reproduced.

## Hosted workflow

This course simulation uses local task files and work logs instead of new
GitHub Issues, PRs, or hosted comments, per the project owner's workflow.
Git commits use the requested simulated schedule; that is separate from
the actual work and push timestamps recorded by GitHub.
