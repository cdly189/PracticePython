"""
If everyone attending shakes hands exactly one time with every other attendee,
how many handshakes are there?
"""


# Solution:
def handshake(n):
    return (n*(n-1))/2


# Test
print(handshake(1))
print(handshake(2))
print(handshake(3))
print(handshake(4))

# Return
# 0
# 1
# 3
# 6