"""
A program that prints out all the elements of the list that are less than 5
Ask a user to enter a number and return a list that is smaller than this number
"""
orgi_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_five = []
user_list = []

# Loop through the original list and add to the new list if element is less than 5
for num in orgi_list:
    if num < 5: # Compare numbers against 5
        less_five.append(num)

print(less_five)

# A list contains all elements that is smaller than user input number
user_num = int(input("Enter a number: "))
for i in orgi_list:
    if i < user_num:
        user_list.append(i)
print(user_list)
