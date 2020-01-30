some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []

for letter in some_list:
    if some_list.count(letter) > 1:
        if letter not in duplicate:
            duplicate.append(letter)


print(duplicate)
