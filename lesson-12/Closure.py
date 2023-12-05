def arcade(name):
    coins = 5

    def game():
        nonlocal coins 
        coins -= 1

        if coins > 1:
            print("\n" + name + " has " + str(coins) + " conis left")
        elif coins == 1:
            print("\n" + name + " has " + str(coins) + "coin left")
        else:
            print(name + " is out of coins")

    return game

Anav = arcade("Anav")
Anav()
Anav()
Anav()

Veer = arcade("Veer")
Veer()
Veer()
Veer()
Veer()





