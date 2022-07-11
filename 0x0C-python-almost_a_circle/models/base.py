#!/usr/bin/python3
"""
    base module
"""

class Base:
    """
        class Base is the 'base' of all other classes in this project. Its goal is to manage
        'id' attribute in all future classes and avoid duplicating the same code and by extension, the same bugs
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            initializing function of the class
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

