#!/usr/bin/env python3

import random


def guess_number():
    print("Welcome to the Number Guessing Game!")

    # Get the range of numbers from the user
    lower_bound = 0  # int(input("Enter the upper bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))

    # Generate a random number within the specified range
    secret_number = random.randint(lower_bound, upper_bound)

    # Initialize variables
    attempts = 0
    guessed = False

    while not guessed:
        user_guess = int(input("Guess the number: "))
        attempts += 1

        if user_guess < secret_number:
            print("Higher!")
        elif user_guess > secret_number:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            guessed = True

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no) [yes]: ").strip().lower() or 'yes'
    if play_again == 'yes' or play_again == 'y':
        guess_number()
    else:
        print("Thank you for playing!")


# Run the game
guess_number()
