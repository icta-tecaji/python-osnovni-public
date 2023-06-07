import math


def pretvornik(x, mode):
    if mode == "deg2rad":
        return math.radians(x)
    else:
        return math.degrees(x)
