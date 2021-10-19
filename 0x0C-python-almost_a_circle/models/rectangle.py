#!/usr/bin/python3
"""
A module for rectangle which inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """ New class rectangle which inherits from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        """ Constructor for rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        else:
            self.__width = value

    @property
    def height(self):
        """ gets the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        else:
            self.__height = value

    @property
    def x(self):
        """ gets the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        else:
            self.__x = value

    @property
    def y(self):
        """ gets the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        else:
            self.__y = value
