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
    print_symbol = "#"

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
        return ((str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """Returns formal string representation..."""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Called at instance deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger of two rectangles.
        Args:
            rect_1: This represents the first rectangle
            rect_2: This represents the second rectangle
        Raises:
            TypeError: if rec_1 and or rect_2 are not instance of Rectangle.
        Returns:
            The rectangle with the largest area of rect_1 if the are same
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance((rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
