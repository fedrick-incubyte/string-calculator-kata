class StringCalculator:
    def add(self, numbers: str):
        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            header, numbers = numbers.split("\n", 1)
            delimiter = header[2]
        else:
            numbers = numbers.replace("\n", ",")

        parts = numbers.split(delimiter)
        return sum(int(num) for num in parts if num.strip().isdigit())
