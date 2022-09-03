"""
Given a list. Write one line of Python that takes this list a and makes a new list that
has only the even elements of this list in it
"""

orgi_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_list = [x for x in orgi_list if x % 2 == 0]    # Use modulo operator to filter even numbers

print(even_list)
