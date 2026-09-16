# Python program for fibonacci series for provided numeber 

def fibonacci(n):
    if n < 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_second(n):
    if n < 0:
        return "Incorrect input"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci(9))

if __name__ == "__main__":
    print("Provide the number for fibonacci series:")
    try:
        n = int(input())
        # We must print the result of the function call
        result = fibonacci(n)
        print(f"The Fibonacci number at position {n} is: {result}")
    except ValueError:
        print("Please enter a valid integer.")
