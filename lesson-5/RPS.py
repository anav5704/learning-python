import sys
import random
from enum import Enum

class RPS(Enum): 
    ROCK = 1
    PAPER = 2
    SCISSORS = 3    

print("")

playerChice = input("Enter... \n 1. Rock \n 2. Paper \n 3. Scissors \n\n") # Game instructionsj
choice = int(playerChice) # Change type from string to interger

if choice < 1 or choice > 3: 
    sys.exit("Invalid input") # Exit program with message0

AI_choice = random.choice("123") # Random number from 1 -3
ai = int(AI_choice) # Change type from string to interger

print("You chose " + str(RPS(choice)).replace("RPS.", "" ).lower())
print("Python AI chose " + str(RPS(ai)).replace("RPS.", "" ).lower())

# User win conditions
if choice == 1 and ai == 3: 
    print("You win! 🎉")

elif choice == 2 and ai == 1: 
    print("You win! 🥳")

elif choice == 3 and ai == 2: 
    print("You win! 🎊") 
# Draw
elif choice == ai: 
    print("Draw! 😵")

# Python AI I win conditionn
else: 
    print("Python AI wins! 🤖")

