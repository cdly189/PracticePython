"""
Write a program that returns a list that contains only the elements that are
common between the lists using list comprehension
I also demonstrate the benefit of using comprehension over loop
"""

import random
import time

random.seed(111)    # Set seed so numbers don't change every time we run program

list1 = random.sample(range(100), 20)    # A list of 20 numbers chosen randomly between 0 and 100
list2 = random.sample(range(100), 30)

start_compre = time.time()    # We want to measure the time it takes to run list comprehension
# Loop through list1, if that number is also in list2
overlap_compre = [num for num in list1 if num in list2]
end_compre = time.time()
print(overlap_compre)
print("Time using comprehension is ",end_compre-start_compre)

overlap = []
start_for = time.time()
for num in list1:
    if num in list2:
        overlap.append(num)
end_for = time.time()
print(overlap)
print("Time using for loop is ",end_for-start_for)




