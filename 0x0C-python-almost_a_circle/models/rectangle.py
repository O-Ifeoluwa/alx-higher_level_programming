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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        def type_check(self, attr, value:obj, isgreater=False):
            """validates all setter methods and instantiation excluding 'id'"""
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(attr))
            if not isgreater:
                if value <= 0:
                    raise ValueError("{} must be > 0".format(attr))
                else:
                    if value < 0:
                        raise ValueError("{} must >= 0".format(attr))
        
        @property
        def width(self):
            """width property"""
            return self.__width

        @width.setter
        def width(self, width):
            """width setter"""
            self.type_check('width', width)
            self.__width = width

        @property
        def height(self):
            """height property"""
            return self.__height

        @height.setter
        def height(self, height):
            """height setter"""
            self.type_check('height', height)
            self.__height = height

        @property
        def x(self):
            """x property"""
            return self.__x

        @x.setter
        def x(self, x):
            """x setter"""
            self.type_check('x', x, True)
            self.__x = x

        @property
        def y(self):
            """y property"""
            return self.__y

        @y.setter
        def y(self, y):
            """y setter"""
            self.type_check('y', y, True)
            self.__y = y


        def area(self):
            """returns the area of the Rectangle instance"""
            return self.width * self.height

         def display(self):
             """Prints the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return [print("") for y in range(self.y)]
        for he in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for wi in range(self.width)]
            print("")

        def __str__(self):
            """returns [rectangle](<id>) <x>/<y> -<width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

        def update(self, *args, **kwargs):
            """assigns an argument to each attribute"""
            if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

        def to_dictionary(self):
            """returns a dictionary representation of a rectangle"""
            return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
