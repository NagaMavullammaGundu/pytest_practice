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
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]