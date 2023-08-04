#!/usr/bin/python3
"""a base moduleclass"""


class meta_class(type):
    """a meta class"""
    def __dir__(cls):
        return [attr for attr in super().__dir__() 
                if attr != "__init_subclass__"]

class BaseGeometry(metaclass=meta_class):
    """a method that excludes the __init_subclass__ from the dir"""

    def __dir__(cls) -> None:
        """this method exclude th init subclass from the dir"""
        attributes = super().__dir__()
        return [attribute for attribute in attributes 
                if attribute != "__init_subclass__"]

    """a method that calculates the area but is not implemented"""
    def area(self):
        """an exception raised"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        value: validating the value
        """
        self.name = "name"
        if type(value) is int:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
            else:
                self.value = value
        else:
            raise TypeError("{} must be an integer".format(name))



"""a subclass Rectangle"""
class Rectangle(BaseGeometry):

    """a method that excludes the __init_subclass__ from the dir"""
    def __dir__(cls) -> None:
        """ excluding the ini subclassin thedir"""
        attributes = super().__dir__()
        return [attribute for attribute in attributes 
                if attribute != "__init_subclass__"]

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """the area of the rectangle implemented"""
        return self.__width * self.__height

    def __str__(self):
        """print out rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


"""a subclas Square that inherits from the class Rectangle"""
class Square(BaseGeometry):
    """a method that excludes the __init_subclass__ from the dir"""
    def __dir__(cls):
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != "__init_subclass__"]

    def __init__(self, size):
        """instantiate with size whic is private"""
        super().__init__() 
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """calculating the areaof the shape"""
        return self.__size ** 2