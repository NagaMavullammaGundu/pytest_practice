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


@pytest.mark.parametrize(
    "inputlist,output",
    [
        ([1, 2, 60, 54], 60),
        ([5, 6.9, 4.3, 7.0, 2.3, 45.5, 4.3], 45.5),
        ([-11.4, -1.0, -2.0, -3.0, -4.0 - 10.0, -9.6], -1.0),
    ],
)
def test_findmax(inputlist, output):

    assert my_function.find_max(inputlist) == output


def test_findmax_strings():
    with pytest.raises(TypeError, match=r"All elements must be numbers"):
        assert my_function.find_max(["hi", "hello"])


def test_findmax_empty():

    with pytest.raises(ValueError, match=r"The list cannot be empty"):
        assert my_function.find_max([])


@pytest.mark.parametrize(
    "input_list,output_list",
    [
        ([11, 2, 3, 2, 11, 4, 5, 6, 6, 6, 5], [2, 3, 4, 5, 6, 11]),
        # (["Apple","banana","Apple"],["banana","Apple"])
    ],
)
def test_remove_duplicates(input_list, output_list):
    assert my_function.remove_duplicates(input_list) == output_list


@pytest.mark.parametrize(
    "a,b,operation,output",
    [
        (5, 3, "add", 8),
        (5, 3, "subtract", 2),
        (5, 3, "multiply", 15),
        # (5,3,"divide",2.66),
        (5.3, 3.3, "add", 8.6),
        (5.3, 3.3, "subtract", 2.0),
        (5.3, 3.3, "multiply", 17.49),
        # (5.3,3.3,"divide",1.60)
    ],
)
def test_calculator(a, b, operation, output):
    assert my_function.calculator(a, b, operation) == output


# def test_calculator_strings():
#   with pytest.raises(ValueError,match = r"Invalid operation"):
#       assert my_function.calculator("hihi","ki","add")///


@pytest.mark.parametrize(
    "inputstring,outputlength",
    [("Apple", False), ("Banana", False), ("abcdef", True), ("bB", True)],
)
def test_unique_characters(inputstring, outputlength):
    assert my_function.has_unique_characters(inputstring) == outputlength


def test_int():
    with pytest.raises(TypeError, match=r"Input must be a string"):
        assert my_function.has_unique_characters(123)


@pytest.mark.parametrize(
    "inputstring,outputlength",
    [
        ("Apple", ["A", "P", "P", "L", "E"]),
        ("Banana", ["B", "A", "N", "A", "N", "A"]),
        ("abcdef", ["A", "B", "C", "D", "E", "F"]),
        ("bB", ["B", "B"]),
        (["madhu", "mavullu"], ["MADHU", "MAVULLU"]),
    ],
)
def test_to_uppercase(inputstring, outputlength):
    assert my_function.to_uppercase(inputstring) == outputlength


def test_to_upperInt():
    with pytest.raises(TypeError, match=r"All elements must be strings"):
        assert my_function.to_uppercase([21, 3, 4, 0, 1])

@pytest.mark.parametrize(
    "inputstring1,inputstring2,outputlength",
    [
        ([2,4,2]),
        (3,15,3),
        (24,72,24)
        
    ]
)

def test_gcd(inputstring1,inputstring2,outputlength):
    assert my_function.gcd(inputstring1,inputstring2) == outputlength

def test_gcd_string():
    with pytest.raises(TypeError, match=r"Inputs must be integers"):
        assert my_function.gcd("madhu","madhuu")
def test_gcd_float():
    with pytest.raises(TypeError, match=r"Inputs must be integers"):
        assert my_function.gcd(5.5,6.6)