# Code Review Checklist - GradeBook

Use this checklist for every Pull Request. Tick each item while reviewing.

## 1. Correctness
- [ ] Does the code do what the PR description claims?
- [ ] Are boundary values handled correctly (0, 100, empty roster, 1 student)?
- [ ] Are there off-by-one errors in loops, comparisons (`>` vs `>=`) or formulas?

## 2. Tests
- [ ] Is there at least one new or updated test for the change?
- [ ] Do tests check real outputs (not just "no exception raised")?
- [ ] Are edge cases and error paths tested (empty input, invalid score, single item)?

## 3. Readability
- [ ] Are function and variable names clear and meaningful?
- [ ] Does every public function have a docstring?
- [ ] Is there any magic number or confusing logic that needs a comment or a constant?

## 4. Design
- [ ] Does the change fit the existing structure of GradeBook?
- [ ] Is there duplicated code that can be reused or moved to a helper?
- [ ] Does each function do only one job (single responsibility)?

## 5. Risk
- [ ] Is user input validated (type, range) before use?
- [ ] Can the change break existing behaviour (backward compatibility)?
- [ ] Any performance problem (e.g. sorting or looping over the whole roster repeatedly)?

---

## Lessons Learned (fill after Task 5)
- Checklist item that caught the most valuable issue: _TODO_
- One checklist item I would add next time: _TODO_
