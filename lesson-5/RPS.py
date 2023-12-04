from enum import Enum
import random
import sys

def playGame():
    class RPS(Enum): 
        ROCK = 1
        PAPER = 2
        SCISSORS = 3   

    playerChice = input("\nEnter... \n 1. Rock \n 2. Paper \n 3. Scissors \n\n") # Game instructionsj
    choice = int(playerChice) # Change type from string to interger

    if playerChice not in ["1", "2", "3"]:
        print("Option not valid")
        return playGame()

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
        
    print("\nWanna play again(y/n)?")
    while True:
        playAgain = input()
        if playAgain.lower() not in ["y", "n"]:
            continue
        else:
            break

    if playAgain == "y":
        return playGame()
    
    elif playAgain == "n": 
        sys.exit("Bye Bye!")

playGame()