import re

MAXIMUM_ADDABLE_VALUE = 1000


class NegativeNumberError(ValueError):
    pass


class StringCalculator:
    def __init__(self):
        self._called_count = 0

    def add(self, numbers: str) -> int:
        self._called_count += 1
        if not numbers:
            return 0

        nums = self._parse_numbers(numbers)
        self._raise_if_negatives(nums)
        
        return sum(n for n in nums if n <= MAXIMUM_ADDABLE_VALUE)

    def _parse_numbers(self, numbers: str) -> list[int]:
        delimiters = [",", "\n"]
        body = numbers

        if numbers.startswith("//"):
            delimiter_header, body = numbers.split("\n", 1)
            delimiters = self._get_delimiters(delimiter_header) + ["\n"]

        sorted_delimiters = sorted(delimiters, key=len, reverse=True)
        pattern = "|".join(re.escape(delimiter) for delimiter in sorted_delimiters)
        return [int(token) for token in re.split(pattern, body) if token.strip()]

    def _get_delimiters(self, header: str) -> list[str]:
        if header.startswith("//[") and header.endswith("]"):
            return header[3:-1].split("][")
        return [header[2]]

    def _raise_if_negatives(self, nums: list[int]):
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise NegativeNumberError(f"negatives: {', '.join(map(str, negatives))}")

    def get_called_count(self) -> int:
        return self._called_count

