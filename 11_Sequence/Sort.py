# Sort function 

#Sorted() function is used to sort the list in ascending order but works by making a copy of the list and sorting instead of in-place 
# sort method does sort in-place
pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
srt = sorted(numbers)
print(srt)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)