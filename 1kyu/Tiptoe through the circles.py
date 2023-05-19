# from typing import NamedTuple
#
# class Point(NamedTuple):
#     x: float
#     y: float
#
#
# class Circle(NamedTuple):
#     ctr: Point
#     r: float
#
#
# def shortest_path_length(a: Point, b: Point, c: list[Circle]) -> float:
#     '''Returns length of shortest route from a to b, avoiding the interiors of the circles in c.'''
#
#     return 0

# a, b = Point(-3, 1), Point(4.25, 0)
#     c = [Circle(Point(0,0), 2.5), Circle(Point(1.5,2), 0.5), Circle(Point(3.5,1), 1), Circle(Point(3.5,-1.7), 1.2)]
#     actual = solution.shortest_path_length(a, b, c)
#     test.assert_approx_equals(actual, 9.11821650244, margin=max_error)
import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle


# fig = plt.figure(figsize=(70, 4))
# fig = plt.figure()
# ax = fig.add_subplot()
# # ax.plot(-3, 1, 'o-r', alpha=0.7, label="first", lw=5, mec='b', mew=0, ms=10, marker='.')
# ax.plot(-3, 1, '.-b', alpha=0.7, ms=5)
# ax.plot(4.25, 0, '.-b', alpha=0.7, ms=5)
#
# # rect = Rectangle((0, 0), 2.5, 0.5, facecolor='g')
# # ax.add_patch(rect)
# circle1 = Circle((0, 0), 2.5, color='y', alpha=0.5)
# circle2 = Circle((1.5, 2), 0.5, color='y', alpha=0.5)
# circle3 = Circle((3.5, 1), 1, color='y')
# circle4 = Circle((3.5, -1.7), 1.2, color='y')
# ax.add_patch(circle1)
# ax.add_patch(circle2)
# ax.add_patch(circle3)
# ax.add_patch(circle4)
# # ax.set(xlim=(-10, 2), ylim=(-10, 10))
# plt.axis('scaled')
# plt.show()


# @test.it("Long way round")
# def ftest2():
#     a, b = Point(0, 1), Point(0, -1)
#     c = [Circle(Point(0, 0), 0.8), Circle(Point(3.8, 0), 3.2), Circle(Point(-3.5, 0), 3), Circle(Point(-7, 0), 1)]
#     actual = solution.shortest_path_length(a, b, c)
#     test.assert_approx_equals(actual, 19.0575347577, margin=max_error)

def distance(p1, p2):  # расстояние между двумя точками на плоскости
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def len_cathetus(cathetus, hypotenuse):  # Длина катета по гипотенузе и катету
    return (hypotenuse ** 2 - cathetus ** 2) ** 0.5


def len_circle(r):
    return 2 * math.pi * r


def len_sector(r, angle):
    return len_circle(r) * angle / 360


hypotenuse = distance((0, 0), (-3, 1))
print(hypotenuse)
cathetus1 = len_cathetus(2.5, hypotenuse)
print(cathetus1)
print(len_circle(2.5))
print(len_sector(2.5,33.80381))
