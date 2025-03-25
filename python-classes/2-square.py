#!/usr/bin/python3
"""
Square definition
"""


class Square:
    """
    Represents a square with Private instance attribute: size.
    """
    def __init__(self, size=0):
        """
        Initialize the square with the given size.
        Args:
            size (int): The size of the square (default is 0)
        Raises:
              TypeError:If size is  not an integer.
              Value:If size is less than 0.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
             raise TypeError('size must be an integer')
       


