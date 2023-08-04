#!/usr/bin/python3


"""the function prototype"""
def is_same_class(obj, a_class):
    """
        obj: the object
        a_class: the class
    """
    if type(obj) is a_class:
        return True
    else:
        return False