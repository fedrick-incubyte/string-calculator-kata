# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run all tests
pytest test.py

# Run a single test by name
pytest test.py::test_add

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

- `add(numbers: str) -> int` — public entry point; increments call counter, delegates to parsers, raises on negatives, ignores numbers >1000
- `_parse_numbers` — normalizes all delimiters to commas then splits; detects `//...\n` header to extract custom delimiters
- `_get_delimiters` — handles two header formats: single-char `//;\n` and bracket-wrapped `//[**][%%]\n`
- `_check_negatives` — collects all negatives and raises a single exception listing them all
- `get_called_count() -> int` — returns how many times `add` has been called on this instance

### Delimiter format

Custom delimiters are declared in a header on the first line:
- Single char: `//;\n1;2;3`
- Any length: `//[***]\n1***2***3`
- Multiple: `//[*][%]\n1*2%3` or `//[**][%%]\n1**2%%3`

## Development approach

This kata is written TDD-first. Add a failing test before implementing any new behavior.
