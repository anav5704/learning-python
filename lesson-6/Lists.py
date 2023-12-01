# Lists: 1 of 4 Collection types

names = ["Anav", "Rohan", "Veer"]

print("Anav" in names)
print(names[0])
print(names.index("Anav"))

names.append("Indeevar")
names += ["Aaryan"]
names.extend(["Soni"])

names.insert(0, "Danvil")

names.remove("Anav")
del names[0]
print(names.pop())

print(names)    

data = [1, 3, 7, 2, 9, 6, 4, 10, 5, 8]
data.sort(reverse=True)

copyData = data.copy()
anotherCopyData = list(data)

print(data, copyData, anotherCopyData)

print(type(data))


# Tuples: 2 of 4 Collection types aka a constant list

myTuple = tuple(("Anav", "Chand"))
otherTuple = ("Indeevar", "Nair")

print(myTuple, otherTuple)
print(type(myTuple))

