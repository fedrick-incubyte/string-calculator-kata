import pytest
from string_calculator.calculator import StringCalculator

def should_return_zero_for_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0

def should_return_number_itself_for_single_number():
    calculator = StringCalculator()
    assert calculator.add("1") == 1

def should_return_sum_of_two_comma_separated_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,2") == 3

def should_return_sum_of_many_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,2,3") == 6

def should_treat_newline_as_valid_delimiter():
    calculator = StringCalculator()
    assert calculator.add("1\n2,3") == 6

def should_handle_trailing_newline():
    calculator = StringCalculator()
    assert calculator.add("1\n") == 1

def should_support_custom_single_char_delimiter():
    calculator = StringCalculator()
    assert calculator.add("//;\n1;2") == 3

def should_ignore_numbers_greater_than_1000():
    calculator = StringCalculator()
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

def test_add_multiple_delimiters():
    calculator = StringCalculator()
    assert calculator.add("//[*][%]\n1*2%3") == 6

def test_add_multiple_long_delimiters():
    calculator = StringCalculator()
    assert calculator.add("//[**][%%]\n1**2%%3") == 6