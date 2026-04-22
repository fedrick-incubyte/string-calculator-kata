class StringCalculator:
    def add(self, numbers: str):
        if numbers == "":
            return 0
        if "," in numbers:
            return sum(int(num) for num in numbers.split(","))
        return int(numbers)