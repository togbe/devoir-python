__author__ = 'togbe'


from numpy import *
from numbers import Number

def circle_area(radius):
    """
calculate perimeter of a circle from radius.
    :param radius: radius of circle
    :return:the area (unit^2 given radius)
    >>> circle_area(5)
    """
    return pi*radius**2
print(circle_area((5)))

def