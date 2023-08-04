#!/usr/bin/python3
"""a base moduleclass"""


class BaseGeometry:
    """a method that excludes the __init_subclass__ from the dir"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != "__init_subclass__"]

    """a method that calculates the area but is not implemented""" 
    def area(self):
        """an exception raised"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        self.name = "name"
        """
        value: validating the value
        """
        if type(value) is int:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
            else:
                self.value = value
        else:
            raise TypeError("{} must be an integer".format(name))