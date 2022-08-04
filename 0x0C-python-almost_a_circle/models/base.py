#!/usr/bin/python3
"""
    base module
"""
import json
import csv
import turtle

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
        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of argument to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as objnfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [x.to_dictionary() for x in list_objs]
                objnfile.write(Base.to_json_string(list_dicts))

   @staticmethod
   def from_json_string(json_string):
       """returns the list of the JSON string representation json_string:"""
       if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance of the class Base with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_inst = cls(1, 1)
            else:
                new_inst = cls(1)
            new_inst.update(**dictionary)
            return new_inst

     @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""
        filename = cls.__name__ + ".csv"
        content = ""
        text = []
        if list_objs is not None:
            content += ','.join(list_objs[0].to_dictionary().keys())
            content += '\n'
            for lst in list_objs:
                content += ','.join(
                    map(str, lst.to_dictionary().values())
                )
                content += '\n'

        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(content)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in csv"""
         filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as cvsf:
                if cls.__name__ == "Rectangle":
                    field = ["id", "width", "height", "x", "y"]
                else:
                    field = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvf, fieldnames=field)
                list_dicts = [dict([v, int(i)] for v, i in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """opens a window and draws all the rectangles and squares
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
