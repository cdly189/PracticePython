"""
Find the set of divisors of a number and return the largest sum of digit
For example, the set of divisors of 12 is (1,2,3,4,6,12)
The output should be 6
"""


# Solution:
def printDivisors(n):
    i = 1
    num_list = []
    sum_list = []
    while i <= n:
        if n % i == 0:    # Find the set of divisors
            num_list.append(i)
        i = i + 1

    for ele in num_list:
        sum_digit = 0
        for digit in str(ele):    # With string, we can sum the digit
            sum_digit += int(digit)
        sum_list.append(sum_digit)

    print(max(sum_list))


# Test
printDivisors(12)
printDivisors(20)

# Return
# 6
# 5
