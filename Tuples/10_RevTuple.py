"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to reverse  a Tuple.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def to_reverse_tuple():
    """
       Description:
           Function is used to reverse a Tuple.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuples.
    """
    tuplex = tuple("HELLO WORLD")
    _slice = tuplex[::-1]
    logging.debug("The Reversed Tuple is {} ".format(_slice))


if __name__ == "__main__":
    to_reverse_tuple()