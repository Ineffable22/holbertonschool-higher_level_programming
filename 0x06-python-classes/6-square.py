#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square that defines a square:
        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0)"""
    def __init__(self, size=0, position=(0, 0)):
        """Size and position are private attribute"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """property of size"""
        return self.__size

    @size.setter
    def size(self, new_size):
        """setter of size"""
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    @property
    def position(self):
        """Position of sqare"""
        return self.__position

    @position.setter
    def position(self, new_position):
        """setter position property"""
        if not isinstance(new_position, tuple) or len(new_position) != 2\
                or not isinstance(new_position[0], int) \
                or not isinstance(new_position[1], int) \
                or new_position[0] < 0 or new_position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = new_position

    def area(self):
        """Public instances  method:
            * Return: The current  square are"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print Square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print(' ' * self.position[0], end="")
                print('#' * self.size)
