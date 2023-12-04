name = "Anav" # Global scope
number = 2

print("Gloabl", name)

def another():
    color = "Red"
    
    def greet(name):
        global number
        number += 3

        nonlocal color
        color = "Cyan"

        print("Local", name, number, color) # Local local scope

    greet("Anav")
another()
 