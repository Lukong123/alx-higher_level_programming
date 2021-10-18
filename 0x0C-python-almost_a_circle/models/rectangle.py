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

