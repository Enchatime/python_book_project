phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

index = ["D", "'", "i", "c", "!"]

for i in index:
    plist.remove(i)

plist.pop(-1)
plist.insert(2, ' ')
plist.extend([plist.pop(), plist.pop()])
plist.pop(4)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)