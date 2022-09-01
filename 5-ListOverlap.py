"""
A program that returns a list that contains only the elements that are common
between the lists (without duplicates)
Randomly generate two lists to test this
"""
import random

a = random.sample(range(10, 40), 10)  # Generate 10 random numbers between 10 and 40
b = random.sample(range(4, 20), 10)

print(list(set(a) & set(b)))  # Using set, it return unique set of numbers
