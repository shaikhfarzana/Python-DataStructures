"""
@Author: Farzana Shaikh
@Date: 14-01-2022 04:00AM
@Last Modified by: Farzana Shaikh
@Last Modified time: 14-01-2022 04:00AM
@Title : Tuple in Python(Program to create the colon of a Tuple.)
"""

from copy import deepcopy
import logging
logging.basicConfig(level=logging.DEBUG)


def to_create_colon_tuple():
    """
       Description:
           Function is used to create a colon of Tuple.
       Parameter:
          No parameter required.
       Return:
           Returns nothing but prints the Tuples.
    """
    # create a tuple
    tuplex = ("HELLO", 5, [], True)
    logging.debug("The Original tuple is {}".format(tuplex))

    # make a copy of a tuple using deepcopy() function
    tuplex_colon = deepcopy(tuplex)
    tuplex_colon[2].append(50)
    logging.debug("The Modified tuple is {}".format(tuplex_colon))
    logging.debug("The Original tuple is {}".format(tuplex))


if __name__ == "__main__":
    to_create_colon_tuple()