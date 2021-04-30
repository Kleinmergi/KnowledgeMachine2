import math


def abst(x, y, u, w):
    return math.sqrt(math.pow(x - u, 2) + math.pow(y - w, 2))


def sign(x):
    if x < 0:
        return -1
    return 1