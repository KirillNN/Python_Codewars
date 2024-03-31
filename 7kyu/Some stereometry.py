from math import pi, sqrt


def stereometry(r, h):
    area = round(4 * pi * r ** 2, 3)
    r_circle = sqrt(r ** 2 - h ** 2)
    area_circle = round(pi * r_circle ** 2, 3)
    length_circle = round(2 * pi * r_circle, 3)
    return area, area_circle, length_circle


print(stereometry(2, 1))
