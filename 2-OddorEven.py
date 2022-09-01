"""
Ask the user for a number. Tell if it is a even or odd number
Ask for another number and determine if the first number is divided by the second number 
"""

num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))

# Check if divisible by 4
if num % 4 == 0:
    print(num, "is a multiple of 4")
# Check even number
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)