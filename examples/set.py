import pprint                     #ouput beautifier

vovels = {'a', 'e', 'i', 'o', 'u'}
word = input('Word: ')

found = []

for letter in word:
    if letter in vovels:
        if letter not in found:
            found.append(letter)
for vovel in found:
#    u = vovels.union(set(word))          #merge of 2 sets
#    u = vovels.difference(set(word))     #difference between 2 sets
    u = vovels.intersection(set(word))    #inner join of 2 sets
    pprint.pprint(u)

