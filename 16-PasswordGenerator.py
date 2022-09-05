"""
A password generator
The passwords should be random, generating a new password every time the user
asks for a new password
Strong passwords have a mix of lowercase letters, uppercase letters, numbers,
and symbols
"""

import string
import random

random.seed(123)
letters, numbers, symbols = list(string.ascii_letters), list(string.digits),\
                            list(string.punctuation)    # Use attributes from the string module
userInput = input("How strong would you like your password? (Easy/Medium/Hard) ").capitalize()
# Capitalize() in case user enter lower cap input


def passGen(userInput):
    if userInput == 'Easy':
        ranPass = random.sample(letters,5)    # Pick 5 letters randomly from
        random.shuffle(ranPass)    # Since letters are in alphabetical order, we want to shuffle them

    elif userInput == 'Medium':
        ranPass = random.sample(letters,5) + random.sample(numbers,5)
        random.shuffle(ranPass)

    elif userInput == 'Hard':
        ranPass = random.sample(letters,5) + random.sample(numbers,5) + random.sample(symbols,5)
        random.shuffle(ranPass)

    return "".join(ranPass)    # The original list is separated by whitespace, combine to form a password


print(passGen(userInput))