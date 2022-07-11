#!/usr/bin/python3

"""
    rectangle module
"""
from models.base import Base

class Rectangle(Base):
    """
        rectangle inherits from Base
    """

    def __init__(self, width: int, height:int, x=0, y=0, id=None):
        """
            initializing the function
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y
