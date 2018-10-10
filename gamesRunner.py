import fizzBuzz

#lets the user pick which game they want to play
def start():
    game = 0
    print("Which game would you like to play? Type in the number for that game.\n1) FizzBuzz")
    game = input()
    #runs the file for the chosen game
    if(game == str(1)):
        fizzBuzz.main()
    else:
        print("Please type in a valid number for a game")
        start()

start()

