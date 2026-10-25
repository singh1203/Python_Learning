farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print()
print("Indexing a sequence")
animal_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
goat = animal_list[3]
print(goat)

# print("Indexing a set is not possible")
# goat = farm_animals[3]

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if more_animals == farm_animals:
    print('The sets are equal')
else:
    print('The sets are different')

# Now using List
data = ["blue", "red", "blue", "green", "red", "blue", "white"]
# Create a set from the list, to remove duplicates.
unique_data = sorted(set(data))
print(unique_data)

# Create a list of unique colours, keeping the order they appeared.
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))  # {'blue': None, 'red': None, 'green': None, 'white': None}