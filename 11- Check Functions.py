"""
Write a function to ask the user for a number and determine whether the number is prime or not
"""

user_num = int(input("Enter a number: "))  # Ask for user input


def checkPrime(num):
    if user_num > 1:  # In case user enters number 1
        for i in range(2, num):
            if num % i == 0:  # Prime numbers factor are 1 and itself
                print(user_num, "is not a prime number")
                break
        else:
            print(user_num, "is a prime number")
    else:
        print(user_num, 'is neither prime nor composite')


checkPrime(user_num)
