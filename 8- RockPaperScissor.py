"""
Make a two-player Rock-Paper-Scissors game.
Ask for player plays (using input), compare them, print out a message of congratulations
to the winner, and ask if the players want to start a new game
"""

prompt = "Player 1, what would you like to choose? Rock, Paper or Scissor "
prompt2 = "Player 2, what would you like to choose? Rock, Paper or Scissor "

while True:
    user1 = input(prompt)
    user2 = input(prompt2)

    if user1 == user2:    # Including a case if both players make same decision
        print("We have a tie")

    elif user1 == 'Rock':
        if user2 == 'Scissor':
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    elif user1 == 'Paper':
        if user2 == 'Rock':
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    elif user1 == 'Scissor':
        if user2 == 'Paper':
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    if input("Do you want to start a new game? (Y/N) ") != 'Y':    # stop if player chooses N
        break
