#!/usr/bin/python3
""" inherit_from """


def inherits_from(obj, a_class):
    """ inherit_ from: function
    Args:
        obj (object): Any object to be tested
        a_class : Any class to be tchecked
    Return: True or false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
