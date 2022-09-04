"""
A function that asks the user how many Fibonnaci numbers to generate
"""

nth_term = int(input("How many Fibonacci numbers do you want to generate? "))


def fibonacci_loop(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        a = 1
        b = 1
        for i in range(n - 1):
            a, b = b, a + b
        return a


fib_list = [fibonacci_loop(x) for x in range(1,nth_term+1)]
print(fib_list)