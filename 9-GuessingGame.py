"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random
guess_count = 0    # Define a variable to keep count

while True:
    user_number = input("Please choose a number between 1 and 10 \nType 'exit' to quit: ")
    random_number = random.randint(1,9)    # Randomly generate numbers between 1 and 9

    if user_number == 'exit':    # stop if player chooses exit
        break

    user_number = int(user_number)    # Convert type
    guess_count += 1    # Increase 1 for every loop

    if user_number < random_number:
        print("Your guess is low")

    elif user_number > random_number:
        print("Your guess is high")

    elif user_number == random_number:
        print("Your guess is correct")


print(f"It took {guess_count} trial for you to get it right")