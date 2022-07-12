#!/usr/bin/python3
""" contains the Square class that inherits fron the Rectangle class"""

from rectangle import Rectangle

class Square(Rectangle):
    """ the class square"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """initialization of the square class
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

