"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

user_string = input("Give me a string: ")

backward_string = user_string[::-1]    # Slicing in a reverse order

if user_string == backward_string:
    print("This string is a palindrome")

else:
    print("This string is not a palindrome")



