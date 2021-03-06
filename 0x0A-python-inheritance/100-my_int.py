#!/usr/bin/python3
'''class MyInt that inherits from int'''


class MyInt(int):
    """" this is myint class
    """

    def __eq__(self, value):
        ''' the inverted operator !='''
        return super().__ne__(value)

    def __ne__(self, value):
        '''  the inverted operator =='''
        return super().__eq__(value)
