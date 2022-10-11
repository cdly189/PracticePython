"""
Given two points P(px,py) and Q(qx,qy).
Find a point R where R is a reflection of P across the point Q
"""

# Solution:

def findPoint(px, py, qx, qy):
    """The formula to find a reflection point is 2p - a"""
    rx = 2 * qx - px
    ry = 2 * qy - py
    return rx, ry

# Test
print(findPoint(0,0,1,1))
print(findPoint(1,1,2,2))

# Return
(2,2)
(3,3)