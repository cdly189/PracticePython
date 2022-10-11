"""
Given an area and base, find the height of the triangle so that it has the smallest area
"""

import math


# Solution:
def lowestTriangle(trianglebase, area):
    height = math.ceil(2*area/trianglebase)
    return height


# Test
print(lowestTriangle(4,6))
print(lowestTriangle(2,2))
print(lowestTriangle(17,100))

# Return
# 3
# 2
# 12
