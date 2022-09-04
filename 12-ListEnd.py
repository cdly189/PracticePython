"""
A function that takes a list of numbers and makes a new list of only
the first and last elements of the given list.
"""

import random


def listEnds(aList):
    return [mylist[0],mylist[-1]]    # Using index to choose the first and last element


random.seed(111)    # Lock in numbers
mylist = random.sample(range(20),5)    # A list of 5 taken randomly between 0 and 20
print("List of first and last element\n",listEnds(mylist))
print("An entire list\n",mylist)