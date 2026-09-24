strrr = "The quick brown fox jumps over the lazy dog"

words = strrr.split() # Split the string into a list of words based on whitespace

dicto = {}
for word in words:
    dicto[word] = dicto.get(word, 0) + 1

print(dicto)

# Question asked in interviews about counting word frequency in a string