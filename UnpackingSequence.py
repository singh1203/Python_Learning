# Tuple's are successfully unpacked, the reason is tuples are immutable hence no changes to the elements count.
x, y, z = 1, 2, 76

print("Unpacking a tuple")

data = 1, 2, 76  # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

# This Unpacking of a list will give error, reason actual are 4 element
# And we are unpacking it into 3 variable hence error
print("Unpacking a list")

data_list = [12, 13, 15]
# data_list.append(14)

p, q, r = data_list
print(p)
print(q)
print(r)

# Unpacking the Tuples 

from nested_data import albums

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}, {}, {}".format(index + 1, title, artist, year, songs))
    break