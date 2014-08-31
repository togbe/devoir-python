__author__ = 'togbe'


from numpy import *
from numbers import Number

def circle_area(radius):
    """
    calculate area of a circle from radius.
    :param radius: radius of circle
    :return:
    """
    return pi*radius**2
print("the area of a circle is",circle_area(45))

def circle_perimeter(radius):
    """calculate the perimeter of a circle from radius.
    """
    return pi*radius*2
print("the perimeter of a circle is",circle_perimeter(56))

def square_area(side):
    """
    calculate the area of a square from side
    :param side:
    :return:
    """
    return side**2
print("the area of a square is",square_area(34))

def square_perimeter(side):
    """
    calculate the perimeter of a square from side
    :param side:
    :return:
    """
    return 4*side
print("the perimeter of a square is",square_perimeter(453))

def rectangle_perimeter(length,width):
    """
    calculate the perimeter of rectangle from length and width
    :param length:
    :param width:
    :return:
    """
    return (length+width)*2
print("the perimeter of a rectangle is",rectangle_perimeter(45,78))

def rectangle_area(length,width):
    """
    calculate the area of rectangle from length and width
    :param length:
    :param width:
    :return:
    """
    return length*width
print("the area of a rectangle is",rectangle_area(567,76))

def triangle_perimeter(side1,side2,side3):
    """
    calculate the perimeter of triangle from side1,side2 and side3
    :param side1:
    :param side2:
    :param side3:
    :return:
    """
    return side1+side2+side3
print("the perimeter of a triangle is",triangle_perimeter(59,32,89))

def trapezium_area(side1,side2,height):
    """
    calculate the area of trapezium from side1,side2 and height
    :param side1:
    :param side2:
    :param height:
    :return:
    """
    return (side1+side2)*height*(1/2)
print("the area of a  trapezium is", trapezium_area(67, 19, 12))

def sphere_area(radius):
    """
    calculate the area of sphere from radius
    :param radius:
    :return:
    """
    return 4*pi*radius**2
print("the area of a sphere is",sphere_area(93))

def cube_volume(side):
    """
    calculate the volume of cube from side
    :param side:
    :return:
    """
    return side**3
print("the volume of cube is",cube_volume(67))

def ellipse_area(radius1,radius2):
    """
    calculate the area of ellipse from radius1 and radius2
    :param radius1:
    :param radius2:
    :return:
    """
    return pi*radius1*radius2
print("the area of ellipse is ",ellipse_area(45,79))

def cylinder_volume(radius,height):
    """
    calculate the volume of cylinder from radius and height
    :param radius:
    :param height:
    :return:
    """
    return pi*height*radius**2
print("the volume of cylinder is ",cylinder_volume(13,67))

def cone_area(side,radius):
    """
    calculate the area of cone from side and radius
    :param side:
    :param radius:
    :return:
    """
    return pi*side*radius
print("the area of cone is ",cone_area(34,9))
