class StringCalculator:
    def add(self, numbers: str):
        if numbers == "":
            return 0
        else:
            return sum(int(num) for num in numbers.replace("\n", ",").split(","))
