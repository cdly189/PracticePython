"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

name = input("What is your name? ")
age = int(input("How old are you? "))
turn_hundred = 2022 + 100 - age
print(f"{name.capitalize()} will turn 100 years old in {turn_hundred} years")