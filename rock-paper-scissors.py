# import os
from random import randint

# ------------------------------ Movimientos -----------------------------------------
moves = {
    "0": "Piedra",
    "1": "Papel",
    "2": "Tijera"
}

# ------------------------------ Funciones -----------------------------------------


# def clearScreen():
#     os.system("cls" if os.name == "nt" else "clear")


def validChoice(playerChoice, moves):
    return playerChoice in moves.keys()


def playerPlays():
    print("\n0: Piedra \U0000270A")  # ✊
    print("1: Papel \U0000270B")  # ✋
    print("2: Tijera \U0000270C")  # ✌️

    return input("Ingresa tu elección [0/1/2]: ")


def machinePlays():
    return str(randint(0, 2))


def evaluate(playerChoice, machineChoice):
    if playerChoice == "0" and machineChoice == "2" or\
       playerChoice == "1" and machineChoice == "0" or\
       playerChoice == "2" and machineChoice == "1":
        return "¡Ganaste! :D"

    if playerChoice == "2" and machineChoice == "0" or\
       playerChoice == "0" and machineChoice == "1" or\
       playerChoice == "1" and machineChoice == "2":
        return "Perdiste :("

    return "¡Es un empate!"


def menu():
    playing = True
    while playing:
        print("------------------------- PIEDRA, PAPEL O TIJERA ------------------------")
        playerChoice = playerPlays()

        while not validChoice(playerChoice, moves):
            print("\nIngresa una opción válida, por favor [0/1/2]")
            playerChoice = playerPlays()

        machineChoice = machinePlays()

        print(f"\n[Tú]: {moves[playerChoice]}")
        print(f"[Computador]: {moves[machineChoice]}")

        print(evaluate(playerChoice, machineChoice))
        playing = input("\n¿Quieres jugar de nuevo? [s/n] ")
        playing = True if playing == "s" else print("Gracias por jugar")
        print("")

        # clearScreen()


def run_game():
    # clearScreen()
    menu()


# ------------------------------ Entrypoint -----------------------------------------
if __name__ == "__main__":
    run_game()
