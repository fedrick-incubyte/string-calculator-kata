import pytest
from string_calculator.calculator import StringCalculator, NegativeNumberError


@pytest.fixture
def calculator():
    return StringCalculator()


def should_return_zero_for_empty_string(calculator):
    assert calculator.add("") == 0

def should_return_number_itself_for_single_number(calculator):
    assert calculator.add("1") == 1

def should_return_sum_of_two_comma_separated_numbers(calculator):
    assert calculator.add("1,2") == 3

def should_return_sum_of_many_numbers(calculator):
    assert calculator.add("1,2,3") == 6

def should_treat_newline_as_valid_delimiter(calculator):
    assert calculator.add("1\n2,3") == 6

def should_handle_trailing_newline(calculator):
    assert calculator.add("1\n") == 1

def should_support_custom_single_char_delimiter(calculator):
    assert calculator.add("//;\n1;2") == 3

def should_ignore_numbers_greater_than_1000(calculator):
    assert calculator.add("2,1001") == 2

def should_include_number_exactly_equal_to_1000(calculator):
    assert calculator.add("1000") == 1000

def should_exclude_number_exactly_equal_to_1001(calculator):
    assert calculator.add("1001") == 0

def should_raise_negative_number_error_not_bare_exception(calculator):
    with pytest.raises(NegativeNumberError):
        calculator.add("-1")

def should_raise_when_single_negative_number_provided(calculator):
    with pytest.raises(NegativeNumberError, match=r"negatives: -2"):
        calculator.add("1,-2")

def should_report_all_negatives_in_exception_message(calculator):
    with pytest.raises(NegativeNumberError, match=r"negatives: -2, -3"):
        calculator.add("1,-2,-3")

def should_track_number_of_times_add_is_called():
    calculator = StringCalculator()
    assert calculator.called_count == 0
    calculator.add("1,2")
    calculator.add("3,4")
    assert calculator.called_count == 2

def should_support_multi_char_delimiter_in_bracket_syntax(calculator):
    assert calculator.add("//[***]\n1***2***3") == 6

def should_support_multiple_single_char_delimiters(calculator):
    assert calculator.add("//[*][%]\n1*2%3") == 6

def should_support_multiple_multi_char_delimiters(calculator):
    assert calculator.add("//[**][%%]\n1**2%%3") == 6
