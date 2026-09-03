for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))   
print("Pi is approximately {0:12.50f}".format(22 / 7))    # It contains a placeholder {0:12.50f} where the value of Pi will be inserted.

# {0}: This is a placeholder for the first argument passed to the format method.

# :12.50f: This is a formatting specification. It specifies how the value should be displayed.

# 12: Minimum width of the field. The whole number, decimal point, and fractional part together should take up at least 12 characters.

# .50f: This specifies that the value should be formatted as a floating-point number with 50 digits after the decimal point.

print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))