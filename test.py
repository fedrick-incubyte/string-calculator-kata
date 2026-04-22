from string_calculator.calculator import StringCalculator
def test_add():
    calculator = StringCalculator()
    assert calculator.add("") == 0
    assert calculator.add("1") == 1
    