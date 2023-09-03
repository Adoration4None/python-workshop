import os
from random import randint

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def playerPlays():
    print("\n0: Rock "     + "\U0000270A")  # ✊
    print("1: Paper "    + "\U0000270B")  # ✋
    print("2: Scissors " + "\U0000270C")  # ✌️

    return input("Enter your choice: ")

def machinePlays():
    return str( randint(0, 2) )

def evaluate(playerChoice, machineChoice):
    if playerChoice == "0" and machineChoice == "2" or\
       playerChoice == "1" and machineChoice == "0" or\
       playerChoice == "2" and machineChoice == "1":
        return "YOU WIN! :D"
    
    if playerChoice == "2" and machineChoice == "0" or\
       playerChoice == "0" and machineChoice == "1" or\
       playerChoice == "1" and machineChoice == "2":
        return "YOU LOSE :("
    
    return "IT'S A TIE!"


# ------------------------------ Main instructions -----------------------------------------
moves = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissors"
}

clearScreen()
print("------------------------- ROCK, PAPER, SCISSORS ------------------------")

playing = True

while playing:
    playerChoice = playerPlays()
    machineChoice = machinePlays()

    print(f"\n[You]: {moves[playerChoice]}")
    print(f"[Machine]: {moves[machineChoice]}")

    print( evaluate(playerChoice, machineChoice) )
    playing = input("\nPlay again? [y/n] ") == "y"
    clearScreen()


    

