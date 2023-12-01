# Dictionaries: 3 of 4 Collection types

car = {
    "name": "Corvette",
    "brand": "Chevrolet",
}

car2 = dict(name="Regera", brand="Konigsegg")

print(car, car2)
print(type(car))


# Item access

print(car["name"])
print(car.get("brand"))


# Acess all

print(car.keys())
print(car.values())


# Change values

car["brand"] = "Toyota"
print(car)

del car["brand"]
del car2
print(car)


# Copy by referece

car3 = car
car3["Engine"] = "v8"
print(car)


# Nesting

person = {
    "name": "Anav"
}

person2 = {
    "name": "Rohan"
}

group = {
    "members": [person, person2]
}

print(group["members"][0]["name"])
