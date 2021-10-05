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
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializing the Rectangle class with width and height"""

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculates the area of a rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

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

    def __str__(self):
        """Returns string representation."""

        if not self.width or not self.height:
            return ""
        return (("#" * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """Returns formal string representation..."""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Called at instance deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
