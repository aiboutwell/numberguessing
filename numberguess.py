# Author: Amanda Boutwell
#
# Import random number function to generate a random number.
import random
# Import os to clear the screen
import os

def num_guess(x, random_number):
    myguess = 0

    # Loop until the guess is equal to the random number
    while (random_number != myguess):
        try:
            myguess = int(input(f"\nGuess a number between 1 and {x}: ").strip())
            if myguess == random_number:
                print("\nCONGRATULATIONS: You guessed the correct number.\n")
            elif myguess < random_number:
                print("\nSorry.  Your guess is too LOW.  Please try again.\n")
            elif random_number < myguess <= x:
                print("\nSorry. Your number is too HIGH.  Try again.\n")
            elif myguess < 1 or myguess > x:
                print(f"\nERROR: Your number should be between 1 and {x}. Please try again.\n")
        except ValueError:
            print(f"\nERROR: You did not chose a number. Please try again\n")


def get_random():
    # Allow the user to pick the highest number in the guessing range.
    #Then let the computer choose a random number.
    x = 0
    random_number=0
    while True:
        try:
            x=int(input("Please choose the maximum number possible for guessing range: "))
        except ValueError:
            print(f"\nERROR: Your chose was not a number.  Please try again.")
        else:
            break
    random_number = random.randint(1, x)
    print(f"random_number is {random_number}")


    return x, random_number


def game_play():
    # clear the screen and run the game
    os.system("cls")
    x, random_number = get_random()
    num_guess(x, random_number)

# Call game_play for the first run
game_play()
# continue to play the game until the user decides to end the game.
while True:
    again = str(input("\nWould you like to play again? (Y/N): ").upper().strip())
    if again == "Y":
        game_play()
        continue
    elif again == "N":
        print("Good Bye.")
        break
    else:
        print("\nPlease enter either Y or N")
