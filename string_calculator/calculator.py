class StringCalculator:
    def add(self, numbers: str):
        if numbers == "":
            return 0
        else:
            return sum(
                int(num) if num.isdigit() else 0
                for num in numbers.replace("\n", ",").split(",")
            )
