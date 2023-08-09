#!/usr/bin/python3
""" creating a class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class inherit from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation method"""
        super().__init__(size, size, x, y, id)
        self.size = size
    

    @property
    def size(self):
        """the getter method"""
        return self.width


    @size.setter
    def size(self, value):
        """The setter method for y"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value


    def __str__(self):
        """the string representation"""
        return str("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))