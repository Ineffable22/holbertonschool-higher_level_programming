#!/usr/bin/python3
"""Class Data"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
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
        self.__data = data

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
        node = Node(value)
        tmp = self.head
        current = tmp
        if self.head is None or tmp.data > value:
            node.next_node = self.head
            self.head = node
        else:
            while current.data < value:
                if current.next_node is None:
                    current.next_node = node
                    return
                tmp = current
                current = current.next_node
            node.next_node = current
            tmp.next_node = node

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
