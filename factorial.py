def factorial(number: int) -> int:
    """
    factorial of a number.
    
    :param number: The number whose factorial needed.
    :return: The resultant factorial of number.
    """
    
    result = 2;
    if number <= 1:
        return 1
        
    for i in range(3, number + 1):
        result *= i
        
    return result
    
for i in range(36):
    print(i, factorial(i))

# def factorial(n: int) -> int:
#     """Return n! (0! is 1)."""
#     if n <= 1:
#         return 1
 
#     result = 2
#     for x in range(3, n + 1):
#         result *= x
 
#     return result
 
 
# for i in range(36):
#     print(i, factorial(i))

# Recursivre approch 
def factorial_recursive(n: int) -> int:
    """
    Return n! (0! is 1).
 
    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.
    """
    if n <= 1:
        return 1
 
    return n * factorial(n - 1)


for i in range(36):
    print(i, factorial(i))