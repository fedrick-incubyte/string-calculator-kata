from string_calculator.calculator import StringCalculator
def test_add():
    calculator = StringCalculator()
    assert calculator.add("") == 0
    assert calculator.add("1") == 1
    assert calculator.add("1,2") == 3
    assert calculator.add("1,2,3") == 6
    assert calculator.add("1\n2,3") == 6
    assert calculator.add("1\n") == 1