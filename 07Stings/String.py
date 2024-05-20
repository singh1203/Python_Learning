print("Hello " * 3 + "World") #Hello Hello Hello World
today = "friday"
print("day" in today)        # True
print("day" not in today)    # False
print("fri" in today)        # True

age = 24
print("My age is " + str(age) + " years")  # Here we are coerced the age into string
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31, "January", "March", "May", "July", "August", "October", "December"))
print("jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}".format(28, 30, 31))