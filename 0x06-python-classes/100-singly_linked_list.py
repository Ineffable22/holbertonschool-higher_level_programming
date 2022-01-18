#!/usr/bin/python3
"""Class Data"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initilizes the data"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data to a value."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node to a value."""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""Class SinglyLinkedList"""


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Initilizes the data"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
        in the list (increasing order)
        """
        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node and ((tmp.next_node).data < value)):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Return a string with singly linked list"""
        value = ""
        tmp = self.__head
        while tmp:
            value += str(tmp.data)
            tmp = tmp.next_node
            if tmp:
                value += '\n'
        return value
