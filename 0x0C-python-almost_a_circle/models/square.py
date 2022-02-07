#!/usr/bin/python3
"""
And now, the Square!
Class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the data"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieves the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size to a value"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string with rectangle to stdout"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, list(self.__dict__.keys())[i], args[i])
        elif kwargs is not None:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return dict(zip(
            ["id", "size", "x", "y"],
            [self.id, self.width, self.x, self.y]
        ))
