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