import re

MAXIMUM_ADDABLE_VALUE = 1000
DEFAULT_DELIMITERS = [",", "\n"]


class NegativeNumberError(ValueError):
    pass


class StringCalculator:
    def __init__(self):
        self._called_count = 0

    def add(self, numbers: str) -> int:
        self._called_count += 1
        if not numbers:
            return 0

        parsed_numbers = self._parse_numbers(numbers)
        self._raise_if_negatives(parsed_numbers)

        return sum(number for number in parsed_numbers if number <= MAXIMUM_ADDABLE_VALUE)

    def _parse_numbers(self, numbers: str) -> list[int]:
        delimiters = list(DEFAULT_DELIMITERS)
        body = numbers

        if numbers.startswith("//"):
            delimiter_header, body = numbers.split("\n", 1)
            delimiters = self._get_delimiters(delimiter_header) + ["\n"]

        sorted_delimiters = sorted(delimiters, key=len, reverse=True)
        pattern = "|".join(re.escape(delimiter) for delimiter in sorted_delimiters)
        return [int(token) for token in re.split(pattern, body) if token.strip()]

    def _get_delimiters(self, delimiter_header: str) -> list[str]:
        if delimiter_header.startswith("//[") and delimiter_header.endswith("]"):
            return delimiter_header[3:-1].split("][")
        return [delimiter_header[2]]

    def _raise_if_negatives(self, parsed_numbers: list[int]):
        negatives = [number for number in parsed_numbers if number < 0]
        if negatives:
            raise NegativeNumberError(f"negatives: {', '.join(map(str, negatives))}")

    def get_called_count(self) -> int:
        return self._called_count
