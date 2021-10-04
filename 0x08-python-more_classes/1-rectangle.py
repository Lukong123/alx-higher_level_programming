#!/usr/bin/python3
"""defines a rectangle class with a private width and height"""


class Rectangle:
    """a rectangle class:
       Args:
           width: width of a rectangle of type int
           height: height of a rectangle of type int
       Raises:
           TypeError: type of both width and height must be int
           ValueError: width and height must be >=0
    """
    
    def __init__(self, width=0, height=0):
        """ Initializing the Rectangle class with width and height"""

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """width getter function"""

        return self.__width

    @width.setter
    def width(self, value):
        """Width setter function"""

        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter function"""

        return self.__height

    @height.setter
    def height(self, value):
        """Height setter function"""

        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
