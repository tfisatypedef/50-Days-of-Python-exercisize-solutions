names = ["kerry", "dickson", "John", "Mary",
"carol", "Rose", "adam"]

poop = []
for k in names:
    #print(k)
    if k.islower():
        poop.append(k)

poopy = tuple(poop)
print(poopy)