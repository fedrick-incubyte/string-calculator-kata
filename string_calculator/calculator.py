class StringCalculator:
    def __init__(self):
        self._called_count = 0

    def add(self, numbers: str):
        self._called_count += 1
        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            delimiter = header[2]
        else:
            numbers = numbers.replace("\n", ",")

        parts = numbers.split(delimiter)
        nums = []
        for num in parts:
            if num.strip():
                nums.append(int(num))

        negatives = [n for n in nums if n < 0]
        if negatives:
            raise Exception(f"negatives: {', '.join(map(str, negatives))}")

        return sum(nums)

    def get_called_count(self):
        return self._called_count

