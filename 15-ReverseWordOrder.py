"""
A function that takes a list and returns a new list that contains
all the elements of the first list minus duplicates.
Using two methods: set and for loop
"""

userString = input("Write a sentence: ")    # Take user input


def ReverseOrderString(userString):
    result = userString.split(" ")    # Seperate words at whitespaces
    reverseString = result[::-1]    # Use slicing index to reverse words order
    newString = " ".join(reverseString)    # Combine words at whitespaces
    print(newString)


ReverseOrderString(userString)