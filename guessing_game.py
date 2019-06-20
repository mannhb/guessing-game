"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    # write your code inside this function.
    print("------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------")
    answer_number = random.randint(1, 10)
    number_of_attempts = []
    while True:
        try:
            number = input("Guess a number from 1 to 10:  ")
            if int(number) > 10 or int(number) < 1:
                print("Please choose a number between 1 and 10. This will count as an attempt. Try again...")
                number_of_attempts.append(number)
                continue
            elif int(number) > answer_number:
                print("It's lower")
                number_of_attempts.append(number)
                continue
            elif int(number) < answer_number:
                print("It's higher")
                number_of_attempts.append(number)
                continue
            elif int(number) == answer_number:
                print("\nYes! You got it!")
                number_of_attempts.append(number)
                print("It took you {} attempt(s) to guess the correct answer!".format(len(number_of_attempts)))
                break
        except ValueError:
            print("Uh Oh! That is not valid input. This will count as an attempt. Please try again...")
            number_of_attempts.append(number)
            continue
    print("\nThe game has closed. Until next time!")



if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
