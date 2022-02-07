#!/usr/bin/python3
"""
First Rectangle
Class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializa the data"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width to a value"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height to a value"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Retrieves the x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x to a value"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Retrieves the y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the x to a value"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Return the current rectangle area"""
        return self.__width * self.__height

    def display(self):
        """Display a square of #"""
        for y in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """Return a string with rectangle to stdout"""
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, (list(self.__dict__.keys()))[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return dict(zip(
            ["id", "width", "height", "x", "y"],
            [self.id, self.width, self.height, self.x, self.y]
        ))
