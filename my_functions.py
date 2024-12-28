def factorial(n):
    if n < 0:
        raise ValueError(f"Given input {n} must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sort_numbers(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers")
    return sorted(numbers)

def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be a number")
    return (celsius * 9/5) + 32

def is_prime(num):
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Input must be a positive integer")
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def reverse_string(s):
    """Utility function for reversing a string
    
    Incase given input is not a string, it will 
    raise a TypeError
    Args:
        s: Input string
    Raises:
        TypeError: input to be string
    Returns: reversed sting
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]

def find_max(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers")
    return max(numbers)

def remove_duplicates(items):
    return list(set(items))

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operation")

def has_unique_characters(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return len(set(s)) == len(s)

def to_uppercase(strings):
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("All elements must be strings")
    return [s.upper() for s in strings]

def gcd(a, b):
    if not all(isinstance(x, int) for x in (a, b)):
        raise TypeError("Inputs must be integers")
    while b:
        a, b = b, a % b
    return abs(a)