#!/usr/bin/python3
"""
    base module
"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of argument"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of argument to a file"""
        filename = cls.__name__ + '.json'
        text = []
        if list_objs is not None:
            for item in list_objs:
                text.append(item.to_dictionary())
            with open(filename, 'w', encoding='utf-8') as f:
                return f.write(Base.to_json_string(text))
