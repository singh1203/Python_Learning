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

SONGS_LIST_INDEX = 3  # constants in Python are written in capital case
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    # print(albums[choice - 1])
    # print(songs_list)
    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))
    print("-"*30)

