class StringCalculator:
    def __init__(self):
        self._called_count = 0

    def add(self, numbers: str) -> int:
        self._called_count += 1
        if not numbers:
            return 0

        nums = self._parse_numbers(numbers)
        self._check_negatives(nums)
        
        return sum(n for n in nums if n <= 1000)

    def _parse_numbers(self, numbers: str) -> list[int]:
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            if header.startswith("//[") and header.endswith("]"):
                delimiters = header[3:-1].split("][")
                for d in delimiters:
                    numbers = numbers.replace(d, ",")
                delimiter = ","
            else:
                delimiter = header[2]
            numbers = numbers.replace("\n", delimiter)
        else:
            delimiter = ","
            numbers = numbers.replace("\n", ",")
        
        return [int(n) for n in numbers.split(delimiter) if n.strip()]

    def _check_negatives(self, nums: list[int]):
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise Exception(f"negatives: {', '.join(map(str, negatives))}")

    def get_called_count(self) -> int:
        return self._called_count

