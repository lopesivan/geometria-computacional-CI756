from math import acos
from math import sqrt

# Its a square with the top edge poked in
points = [
    ( 1.0,  1.0),
    ( 0.0,  0.0),
    (-1.0,  1.0),
    (-1.0, -1.0),
    ( 1.0, -1.0)]


def angle(x1, y1, x2, y2):
    # Use dotproduct to find angle between vectors
    # This always returns an angle between 0, pi
    numer = (x1 * x2 + y1 * y2)
    denom = sqrt((x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2))
    return acos(numer / denom) 


def cross_sign(x1, y1, x2, y2):
    # True if cross is positive
    # False if negative or zero
    return x1 * y2 > x2 * y1

for i in range(len(points)):
    p1 = points[i]
    ref = points[i - 1]
    p2 = points[i - 2]
    x1, y1 = p1[0] - ref[0], p1[1] - ref[1]
    x2, y2 = p2[0] - ref[0], p2[1] - ref[1]

    print('Points', p1, ref, p2)
    print('Angle', angle(x1, y1, x2, y2))
    if cross_sign(x1, y1, x2, y2):
        print('Inner Angle')
    else:
        print('Outer Angle')
    print('')