#!/usr/bin/python3

class Base:
    __nb__objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects++

        self.id = Base.__nb__objects

