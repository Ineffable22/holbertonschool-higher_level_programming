#!/usr/bin/python3
"""Base Class"""
import json
import csv

class Base:
    """Manages id attribute in all classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the data"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = "[]"
        else:
            with open(cls.__name__ + ".json", "w", encoding="utf-8") as fo:
                fo.write(cls.to_json_string([d.to_dictionary()
                                             for d in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as fo:
                return [(cls.create(**d)) for d in cls.from_json_string(fo.read())]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = "[]"
        else:
            with open(cls.__name__ + ".csv", "w", encoding="utf-8") as fo:
                fo.write(cls.to_json_string([d.to_dictionary()
                                             for d in list_objs]))

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as fo:
                return [(cls.create(**d)) for d in cls.from_json_string(fo.read())]
        except:
            return []
