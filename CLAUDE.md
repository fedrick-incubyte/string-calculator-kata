# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run all tests
pytest test.py

# Run a single test by name
pytest test.py::should_return_zero_for_empty_string

# Run tests with verbose output
pytest test.py -v
```

No virtual environment is committed — install pytest manually or via a local venv:
```bash
python3 -m venv .venv && source .venv/bin/activate && pip install pytest
```

## Architecture

This is a single-module Python kata: `string_calculator/calculator.py` contains the `StringCalculator` class, and `test.py` at the root holds all tests (flat structure by design).

### `StringCalculator` class

- `add(numbers: str) -> int` — public entry point; increments call counter, delegates to parser and validator, raises on negatives, ignores numbers > `MAXIMUM_ADDABLE_VALUE`
- `_parse_numbers` — splits the input using `re.split` with all active delimiters (sorted longest-first to avoid partial matches); detects `//...\n` header to extract custom delimiters
- `_get_delimiters` — handles two header formats: single-char `//;\n` and bracket-wrapped `//[**][%%]\n`
- `_raise_if_negatives` — collects all negatives and raises `NegativeNumberError` listing them all
- `called_count` — `@property` returning how many times `add` has been called on this instance

### Module-level constants

- `MAXIMUM_ADDABLE_VALUE = 1000` — numbers above this are excluded from the sum
- `DEFAULT_DELIMITERS = [",", "\n"]` — always-active delimiters; custom headers add to or replace the comma but `\n` is always preserved

### Exception types

- `NegativeNumberError(ValueError)` — raised when any negative number is provided; message format: `"negatives: -2, -3"`

### Delimiter format

Custom delimiters are declared in a header on the first line:
- Single char: `//;\n1;2;3`
- Any length: `//[***]\n1***2***3`
- Multiple: `//[*][%]\n1*2%3` or `//[**][%%]\n1**2%%3`

## Testing conventions

- Test functions use the `should_[expected behavior]_when_[condition]` naming pattern
- `pytest.ini` configures pytest to collect both `test_*` and `should_*` functions
- A `calculator` fixture in `test.py` provides a fresh `StringCalculator` instance per test
- Exception tests use `pytest.raises(NegativeNumberError, match=r"...")` to assert both type and message
- Tests that exercise stateful counting across multiple calls create their own instance rather than using the fixture

## Development approach

This kata is written TDD-first. Add a failing test before implementing any new behavior. Follow the red → green → refactor cycle and commit after each green step.
