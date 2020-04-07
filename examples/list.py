letters = ['t', 'a', 's']
word = input("Enter your word: ")
found = []


for letter in word:
    if letter in letters:
        found.append(letter)  # add to the end of list
        found.remove("t")     # remove from list by string
        found.pop(0)          # remove from list by index (starts from zero)
        found.extend([3, 4])  # add list to the end of list
        found.insert(0, "s")  # add to the start of list (sets index)
print(len(found))

