#!/usr/bin/python3
""" contains the Square class that inherits fron the Rectangle class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ the class square"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """initialization of the square class
        """
        super().__init__(id, x, y, size, size)
        self.__size = size

    @property
    def size(self):
        """Size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of square size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string method"""
        return "[Square ({}) {}/{} - {}".format(id, x, y, size)

    def update(self, *args, **kwargs):
        """updates the class"""
        attr = ['id', 'x', 'y', 'size']
        if args:
            for attri, number in zip(attr, args):
                setattr(self, attri, number)
            elif kwargs:
                for key, value in kwargs.items():
                    if key in attr:
                        setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
