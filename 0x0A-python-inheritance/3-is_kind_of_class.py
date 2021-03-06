#!/usr/bin/python3
""" is_kind_of_class: function """


def is_kind_of_class(obj, a_class):
    """ Return: True if the object is an instance of, or if the object
                is an instance of a class that inherited
                from, the specified class
            False otherwise
    """
    if not isinstance(obj, a_class):
        return False
    return True
