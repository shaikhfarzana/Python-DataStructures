"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to slice a Tuple.)
"""

import logging
logging.basicConfig(level=logging.DEBUG)


def to_slice_tuple():
    """
       Description:
           Function is used to slice a tuple.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuples.
    """
    # create a tuple
    tuple1= (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
    logging.debug("The Tuple is {} ".format(tuple1))
    # used tuple[start:stop] the start index is inclusive and the stop index
    _slice = tuple1[3:5]
    logging.debug("The Sliced Tuple is {} ".format(_slice))
    # if the start index isn't defined, is taken from the beginning of the tuple
    _slice = tuple1[:6]
    logging.debug("The Sliced Tuple is {} ".format(_slice))
    # if the end index isn't defined, is taken until the end of the tuple
    _slice = tuple1[5:]
    logging.debug("The Sliced Tuple is {} ".format(_slice))
    # if neither is defined, returns the full tuple
    _slice = tuple1[:]
    logging.debug("The Sliced Tuple is {} ".format(_slice))
    # The indexes can be defined with negative values
    _slice = tuple1[-8:-4]
    logging.debug("The Sliced Tuple is {} ".format(_slice))
    # create another tuple
    tuplex = tuple("HELLO WORLD")
    logging.debug("The Sliced Tuple is {} ".format(tuplex))
    # step specify an increment between the elements to cut of the tuple
    # tuple[start:stop:step]
    _slice = tuplex[2:9:2]
    logging.debug("The Sliced Tuple is {} ".format(_slice))
    # returns a tuple with a jump every 3 items
    _slice = tuplex[::4]
    logging.debug("The Sliced Tuple is {} ".format(_slice))
    # when step is negative the jump is made back
    _slice = tuplex[9:2:-4]
    logging.debug("The Sliced Tuple is {} ".format(_slice))
    # reversing the tuple
    _slice = tuplex[::-1]
    logging.debug("The Reversed Tuple is {} ".format(_slice))


if __name__ == "__main__":
    to_slice_tuple()
