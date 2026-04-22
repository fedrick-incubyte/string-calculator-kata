import pytest
from string_calculator.calculator import StringCalculator

def test_add():
    calculator = StringCalculator()
    assert calculator.add("") == 0
    assert calculator.add("1") == 1
    assert calculator.add("1,2") == 3
    assert calculator.add("1,2,3") == 6
    assert calculator.add("1\n2,3") == 6
    assert calculator.add("1\n") == 1
    assert calculator.add("//;\n1;2") == 3
    assert calculator.add("2,1001") == 2

def test_add_negative_numbers():
    calculator = StringCalculator()
    with pytest.raises(Exception) as excinfo:
        calculator.add("1,-2")
    assert "negatives: -2" in str(excinfo.value)

def test_add_multiple_negative_numbers():
    calculator = StringCalculator()
    with pytest.raises(Exception) as excinfo:
        calculator.add("1,-2,-3")
    assert "negatives: -2, -3" in str(excinfo.value)

def test_get_called_count():
    calculator = StringCalculator()
    assert calculator.get_called_count() == 0
    calculator.add("1,2")
    calculator.add("3,4")
    assert calculator.get_called_count() == 2

def test_add_any_length_delimiter():
    calculator = StringCalculator()
    assert calculator.add("//[***]\n1***2***3") == 6