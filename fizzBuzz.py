#fizzbuzz

import random
import sys

#checks if the number given is divisible by 3
def checkFizz(number):
    if(number%3 == 0):
        return True
    else:
        return False

#checks if the number given is divisble by 5
def checkBuzz(number):
    if(number%5 == 0):
        return True
    else:
        return False

#runs through what's needed for the player's go
def playerTurn(currentNumber):
    #updates the number and gets the input
    currentNumber = currentNumber + 1
    playerInput = input("Your turn\n")
    #checks if the player correctly said fizzbuzz
    if(checkFizz(currentNumber) and checkBuzz(currentNumber)):
        if(playerInput.lower() != 'fizzbuzz'):
            print("should fizzbuzz")
            print("You lose!")
            return False
        else:
           return computerTurn(currentNumber)
    #checks if the player correctly said fizz
    elif(checkFizz(currentNumber)):
        if(playerInput.lower() != "fizz"):
            print("You lose!")
            return False
        else:
            return computerTurn(currentNumber)
    #check if the player correctly said buzz
    elif(checkBuzz(currentNumber)):
        if(playerInput.lower() != "buzz"):
            print("should buzz")
            print("You lose!")
            return False
        else:
            return computerTurn(currentNumber)
    #otherwise checks the player has enterred the correct number
    else:
       if(playerInput != str(currentNumber)):
           print("You lose!")
           return False
    return computerTurn(currentNumber)
            
#runs through everything needed for the computer's turn
def computerTurn(currentNumber):
    #updates the number
    currentNumber = currentNumber + 1
    #decides if the computer will succeed
    shallSucceed = random.choices([True, False], [0.8, 0.2], k=1)[0]
    #outputs the correct output if it does succeed
    if(shallSucceed):
        if(checkFizz(currentNumber) and checkBuzz(currentNumber)):
            print("FizzBuzz")
        elif(checkFizz(currentNumber)):
            print("Fizz")
        elif(checkBuzz(currentNumber)):
            print("Buzz")
        else:
            print(str(currentNumber))
        return playerTurn(currentNumber)
    #outputs a reasonable incorrect output if it fails
    if(not shallSucceed):
        if(checkFizz(currentNumber) or checkBuzz(currentNumber)):
            print(str(currentNumber))
        else:
            if(checkFizz(currentNumber+1)):
                print("Fizz")
            elif(checkBuzz(currentNumber+1)):
                 print("Buzz")
            else:
                 print(str(currentNumber-1))
        print("You win!")
        return True

def main():
    #picks who starts and starts the game
    computerStart = random.choice([True, False])
    if(computerStart):
        doesWin = computerTurn(0)
    else:
        doesWin = playerTurn(0)
    #responds to who wins
    if(doesWin):
        print("Congrats!")
    else:
        print("Better luck next time!")
    #handles replaying and exiting if the user doesn't want to play again
    playAgain = input("Would you like to play again? (y/n)")
    if(playAgain.lower() == "y"):
        main()
    else:
        sys.exit()

        
            
           
    
