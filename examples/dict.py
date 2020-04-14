## sorted(dictionary) for sorting
#dictionary = {'Name': 'John', 'Age' : '22', 'Country': 'USA'}
#print(dictionary)
#print(dictionary['Name'])

vovels = ['a', 'e', 'i', 'o', 'u']
word = input('Word: ')

found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0


for letter in word:
    if letter in vovels:
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s)')

#######################################

fruits = {}
fruit = input('Fruit: ')

fruits['apples'] = 10

fruits.setdefault(fruit, 0)

if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 0
print(fruits)