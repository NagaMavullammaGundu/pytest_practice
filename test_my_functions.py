import pytest
import my_functions as my_function


# FACTORIAL
@pytest.mark.parametrize(
    "input_number, expected_factorial", [(5, 120), (0, 1), (1, 1), (4, 24)]
)
def test_factorial_one(input_number, expected_factorial):
    result = my_function.factorial(input_number)
    assert result == expected_factorial


def test_factorial_three():
    number = -10
    with pytest.raises(
        ValueError, match=f"Given input {number} must be a non-negative integer"
    ):
        result = my_function.factorial(number)


# PALINDROME
@pytest.mark.parametrize(
    "input_string , expected_result",
    [("AMMA", True), (" AMMA ", True), ("CAT", False), ("cat ", False)],
)
def test_palindrome_two(input_string, expected_result):
    result = my_function.is_palindrome(input_string)
    assert result == expected_result


def test_palindrome_one():
    with pytest.raises(TypeError, match=r"Input must be a string"):
        result = my_function.is_palindrome(1)
