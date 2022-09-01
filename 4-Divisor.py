"""
Create a program that asks the user for a number and then prints out a list of
all the divisors of that number
"""

user_number = int(input("Enter a number: "))
divisor_list = []

range_list = list(range(1,user_number+1))    # List start from 1 because can't divide by 0

for num in range_list:
    if user_number % num == 0:    # user chosen number divides evenly into another number
        divisor_list.append(num)

print(divisor_list)

