class StringCalculator:
    def add(self, numbers: str):
        if numbers == "":
            return 0
        
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers.split("\n", 1)[1]
            parts = numbers.split(delimiter)
        else:
            parts = numbers.replace("\n", ",").split(",")
            
        return sum(int(num) if num.isdigit() else 0 for num in parts)
