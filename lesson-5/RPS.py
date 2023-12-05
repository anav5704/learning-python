from enum import Enum
import random
import sys

def game():
    gameCount = 0
    player_wins = 0
    ai_wins = 0

    def playGame():
        nonlocal player_wins
        nonlocal ai_wins

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
        def decideWinner(choice, ai):
            nonlocal player_wins
            nonlocal ai_wins

            if choice == 1 and ai == 3: 
                player_wins += 1
                return "You win! 🎉"

            elif choice == 2 and ai == 1: 
                player_wins += 1
                return "You win! 🥳"

            elif choice == 3 and ai == 2: 
                player_wins += 1
                return "You win! 🎊"
            # Draw
            elif choice == ai: 
                return "Draw! 😵"

            # Python AI I win conditionn
            else: 
                ai_wins += 1
                return "Python AI wins! 🤖"
            
        gameResult = decideWinner(choice, ai)
        print(gameResult)

        nonlocal gameCount
        gameCount += 1
            
        print("\nGames played:" + " " + str(gameCount))
        print("Your wins: " + str(player_wins) + " |  Python wins: " + str(ai_wins))

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

    return playGame

start = game()
start()