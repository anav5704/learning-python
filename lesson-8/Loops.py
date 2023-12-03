# While loop

value = 0

while value <= 10:
    print(value)
    value += 1
else:
    print("Value is now " + str(value))


# For loop

names = ["Danvil", "Anav", "Shaneel"]
games = ["Valorant", "Apex Legends", "Fprtnite"]

for game in games:
    print(game)

for x in range(0, 101, 10):
    print(x)

for name in names:
    for game in games:
        print(name + " " + game)




