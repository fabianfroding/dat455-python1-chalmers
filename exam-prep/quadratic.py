import math


def quadratic(a, b, c):
    res = []

    discr = b**2 - 4 * a * c

    if discr < 0:
        return []
    elif discr == 0:
        return [-b / (2 * a)]
    else:
        rdiscr = math.sqrt(discr)
        return [(-b - rdiscr) / (2 * a), (-b + rdiscr) / (2 * a)]
    



print(quadratic(5,-10,5))