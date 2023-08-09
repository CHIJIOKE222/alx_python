#!/usr/bin/python3
"""this module contains the base class its objects and methods """


class Base:
    """this base class will serve as a super class to
    other classes in this module"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init__    the class constructor.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects