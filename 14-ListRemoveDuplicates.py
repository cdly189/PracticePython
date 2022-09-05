"""
A function that takes a list and returns a new list that contains
all the elements of the first list minus duplicates.
Using two methods: set and for loop
"""


# A for loop
def distinctListLoop(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y


# Using sets
def distinctSet(x):
    return list(set(x))


mylist = [1, 2, 3, 4, 3, 2, 1]

print(mylist)
print(distinctListLoop(mylist))
print(distinctSet(mylist))
