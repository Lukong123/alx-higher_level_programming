#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
a class Square that inherits from Rectangle (9-rectangle.py):
"""


class Square(Rectangle):
    """
    class square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
