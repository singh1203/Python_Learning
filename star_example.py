numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")


def test_star(*args):
    print(args)  # Prints the tuple i.e (0, 1, 2, 3, 4, 5)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5) # It unpacks the tuple as *args is var keyword argument and
# then prints the element of tuple

print() # Prints the line and default parameter for print function is /n (new line)

test_star() # Prints the empty tuple i.e ()
