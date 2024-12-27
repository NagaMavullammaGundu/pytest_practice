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

#FIBONACCI
@pytest.mark.parametrize("input_number,output_number", [(0, 0), (1, 1), (5, 5), (6, 8)])
def test_fibonacci_two(input_number, output_number):
    result = my_function.fibonacci(input_number)
    print(result)
    assert result == output_number


def test_fibonacci_one():
    with pytest.raises(ValueError, match=r"n must be a non-negative integer"):
        result = my_function.fibonacci(-1)


@pytest.mark.parametrize(
    "input_list , expected_result",
    [
        ([1, 5, 7, 88, 99, 101, 3, 65, 0, 3], [0, 1, 3, 3, 5, 7, 65, 88, 99, 101]),
        (
            [-1, 5, 7, -88, 99, 101, -3, 65, 0, 3],
            [-88, -3, -1, 0, 3, 5, 7, 65, 99, 101],
        ),
        ([], []),
        (
            [-1, 5.8, 7, -88.3, 99, 101.8, -3, 65, 0, 3],
            [-88.3, -3, -1, 0, 3, 5.8, 7, 65, 99, 101.8],
        ),
    ],
)
def test_sort_numbers(input_list, expected_result):
    result = my_function.sort_numbers(input_list)
    assert result == expected_result


def test_sort_numbers_invalid_input():
    with pytest.raises(TypeError, match=r"All elements must be numbers"):
        result = my_function.sort_numbers(["a", "abc", "xyz"])


@pytest.mark.parametrize(
    "inputnumber,expected_output", [(8, 46.4), (5.5, 41.9), (0, 32), (-5.5, 22.1)]
)
def test_CtoF_number(inputnumber, expected_output):
    assert my_function.celsius_to_fahrenheit(inputnumber) == expected_output


def test_CtoF_charachters():
    with pytest.raises(TypeError, match=r"Temperature must be a number"):
        result = my_function.celsius_to_fahrenheit("ABC")


@pytest.mark.parametrize(
    "inputnumber,expectedOutput",
    [(1, False), (2, True), (3, True), (11, True), (15, False), (1, False)],
)
def test_prime(inputnumber, expectedOutput):
    assert my_function.is_prime(inputnumber) == expectedOutput


def test_prime_notnumbers():
    with pytest.raises(ValueError, match=r"Input must be a positive integer"):
        result = my_function.is_prime(-1)

@pytest.mark.parametrize("inputstring,outputString", [("Apple", "elppA")])
def test_reverse_string(inputstring, outputString):
    assert my_function.reverse_string(inputstring) == outputString

@pytest.mark.parametrize("invalid_input",
                         [(100),
                          (100.879),
                          (-100)
                          ])
def test_reverse_invalidNumbers(invalid_input):
    with pytest.raises(TypeError, match=r"Input must be a string"):
        result = my_function.reverse_string(invalid_input)


